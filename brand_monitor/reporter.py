from .schemas import VisibilityReport


def render_markdown_report(report: VisibilityReport) -> str:
    lines = [
        "# Gemini AI Search Brand Visibility Report",
        "",
        f"**Tracked Brands:** {', '.join(report.target_brands)}",
        "",
    ]

    for idx, res in enumerate(report.results, start=1):
        lines.append(f"## {idx}. Query: `{res.query}`")
        lines.append(f"- **Model:** `{res.model_used}`")
        lines.append(f"- **Summary:** {res.grounded_response_summary}")
        lines.append("")
        lines.append("| Brand | Mentioned | Rank | Sentiment | Direct Booking Perks | Notes |")
        lines.append("| :--- | :---: | :---: | :---: | :---: | :--- |")
        for bm in res.brand_mentions:
            mentioned_icon = "✅" if bm.mentioned else "❌"
            rank_str = f"#{bm.rank_position}" if bm.rank_position else "—"
            direct_icon = "✅" if bm.Direct_booking_highlighted else "—"
            lines.append(
                f"| **{bm.brand_name}** | {mentioned_icon} | {rank_str} | {bm.sentiment} | {direct_icon} | {bm.summary_snippet} |"
            )
        if res.citations:
            lines.append("")
            lines.append("**Grounded Sources:**")
            for url in res.citations:
                lines.append(f"- {url}")
        lines.append("")

    return "\n".join(lines)
