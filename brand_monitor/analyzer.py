import json
from typing import List, Optional
from google import genai
from .schemas import BrandMention, QueryAuditResult, VisibilityReport


class BrandVisibilityAnalyzer:
    """Evaluates brand positioning using Gemini Interactions API and Google Search Grounding."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-3.8-flash"):
        self.client = genai.Client(api_key=api_key) if api_key else genai.Client()
        self.model = model

    def audit_query(self, query: str, target_brands: List[str]) -> QueryAuditResult:
        brands_csv = ", ".join(target_brands)
        prompt = (
            f"Search query: '{query}'\n\n"
            f"Target brands to track: {brands_csv}\n\n"
            "Use Google Search to answer the search query objectively as a helpful AI travel/product advisor. "
            "Then evaluate whether each target brand is mentioned, its 1-based rank position among recommendations, "
            "its sentiment (positive/neutral/negative), and whether direct booking / official site perks are noted."
        )

        schema = QueryAuditResult.model_json_schema()
        interaction = self.client.interactions.create(
            model=self.model,
            input=prompt,
            tools=[{"type": "google_search"}],
            response_format=[
                {
                    "type": "json_schema",
                    "json_schema": {
                        "name": "query_audit_result",
                        "schema": schema,
                    },
                }
            ],
            generation_config={"thinking_level": "low"},
        )

        raw_text = interaction.output_text or "{}"
        data = json.loads(raw_text)
        data["query"] = query
        data["model_used"] = self.model

        # Extract search citations from google_search_result steps if present
        citations: List[str] = list(data.get("citations", []))
        for step in getattr(interaction, "steps", []) or []:
            if getattr(step, "type", None) == "google_search_result":
                for item in getattr(step, "results", []) or []:
                    url = getattr(item, "url", None)
                    if url and url not in citations:
                        citations.append(url)
        data["citations"] = citations
        return QueryAuditResult.model_validate(data)

    def run_audit(self, queries: List[str], target_brands: List[str]) -> VisibilityReport:
        results = [self.audit_query(q, target_brands) for q in queries]
        return VisibilityReport(target_brands=target_brands, results=results)
