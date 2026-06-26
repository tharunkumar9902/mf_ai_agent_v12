from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from app.services.compare_service import compare_two_funds

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

def _compare_markdown(result: dict) -> str:
    f1 = result["fund_1"]
    f2 = result["fund_2"]
    lines = [
        f"# Mutual Fund Comparison Report",
        "",
        f"## Fund 1: {f1['scheme_name']}",
        f"- Scheme Code: {f1['scheme_code']}",
        f"- Fund House: {f1.get('fund_house')}",
        f"- Metrics: {f1['metrics']}",
        "",
        f"## Fund 2: {f2['scheme_name']}",
        f"- Scheme Code: {f2['scheme_code']}",
        f"- Fund House: {f2.get('fund_house')}",
        f"- Metrics: {f2['metrics']}",
        "",
        f"## Summary",
        result["summary"],
    ]
    return "\n".join(lines)

def _write_pdf(report_text: str, pdf_path: Path):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(str(pdf_path), pagesize=A4)
    story = []
    for line in report_text.split("\n"):
        if not line.strip():
            story.append(Spacer(1, 8))
        else:
            story.append(Paragraph(line.replace("&", "&amp;"), styles["BodyText"]))
    doc.build(story)

def build_compare_report_files(fund_1: str, fund_2: str):
    result = compare_two_funds(fund_1, fund_2)
    safe_name = f"{fund_1[:20]}_vs_{fund_2[:20]}".replace(" ", "_").replace("/", "_")
    md_path = REPORTS_DIR / f"{safe_name}.md"
    pdf_path = REPORTS_DIR / f"{safe_name}.pdf"

    md_content = _compare_markdown(result)
    md_path.write_text(md_content, encoding="utf-8")
    _write_pdf(md_content, pdf_path)

    return {
        "markdown_file": str(md_path),
        "pdf_file": str(pdf_path),
        "summary": result["summary"]
    }
