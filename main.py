import argparse
import os
from dotenv import load_dotenv
from brand_monitor.analyzer import BrandVisibilityAnalyzer
from brand_monitor.reporter import render_markdown_report


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Monitor brand visibility in AI Search using Google Gemini & Search Grounding."
    )
    parser.add_argument(
        "--brands",
        required=True,
        help="Comma-separated list of brand or hotel names to track.",
    )
    parser.add_argument(
        "--queries",
        required=True,
        help="Comma-separated list of search queries to evaluate.",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("DEFAULT_GEMINI_MODEL", "gemini-3.8-flash"),
        help="Gemini model name (default: gemini-3.8-flash or gemini-4-argon).",
    )
    parser.add_argument(
        "--output",
        default="visibility_report.md",
        help="Output Markdown file path.",
    )
    args = parser.parse_args()

    brands = [b.strip() for b in args.brands.split(",") if b.strip()]
    queries = [q.strip() for q in args.queries.split(",") if q.strip()]

    analyzer = BrandVisibilityAnalyzer(model=args.model)
    report = analyzer.run_audit(queries=queries, target_brands=brands)
    markdown = render_markdown_report(report)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
