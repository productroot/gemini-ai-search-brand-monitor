from brand_monitor.reporter import render_markdown_report
from brand_monitor.schemas import BrandMention, QueryAuditResult, VisibilityReport


def test_render_markdown_report():
    report = VisibilityReport(
        target_brands=["Hotel Grand", "Boutique Oasis"],
        results=[
            QueryAuditResult(
                query="best spa hotels in Warsaw",
                model_used="gemini-3.8-flash",
                grounded_response_summary="Top spa hotels include Hotel Grand with thermal pools.",
                citations=["https://example.com/warsaw-spa"],
                brand_mentions=[
                    BrandMention(
                        brand_name="Hotel Grand",
                        mentioned=True,
                        rank_position=1,
                        sentiment="positive",
                        Direct_booking_highlighted=True,
                        summary_snippet="Ranked #1 for luxury wellness and direct package offers.",
                    ),
                    BrandMention(
                        brand_name="Boutique Oasis",
                        mentioned=False,
                        rank_position=None,
                        sentiment="neutral",
                        Direct_booking_highlighted=False,
                        summary_snippet="Not surfaced in top grounded results.",
                    ),
                ],
            )
        ],
    )
    md = render_markdown_report(report)
    assert "# Gemini AI Search Brand Visibility Report" in md
    assert "| **Hotel Grand** | ✅ | #1 | positive | ✅ |" in md
    assert "https://example.com/warsaw-spa" in md
