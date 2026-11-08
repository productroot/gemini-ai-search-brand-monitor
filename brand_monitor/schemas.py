from typing import List, Optional
from pydantic import BaseModel, Field


class BrandMention(BaseModel):
    brand_name: str = Field(description="Name of the brand evaluated.")
    mentioned: bool = Field(description="Whether the brand appears in the grounded response.")
    rank_position: Optional[int] = Field(
        default=None,
        description="1-based ranking position among recommended options, or None if not ranked.",
    )
    sentiment: str = Field(
        default="neutral",
        description="Sentiment toward the brand: positive, neutral, or negative.",
    )
    Direct_booking_highlighted: bool = Field(
        default=False,
        description="Whether direct website/booking advantages were mentioned.",
    )
    summary_snippet: str = Field(
        default="",
        description="Short excerpt summarizing how the brand was described.",
    )


class QueryAuditResult(BaseModel):
    query: str
    model_used: str
    grounded_response_summary: str
    citations: List[str] = Field(default_factory=list)
    brand_mentions: List[BrandMention] = Field(default_factory=list)


class VisibilityReport(BaseModel):
    target_brands: List[str]
    results: List[QueryAuditResult]
