from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

def generate_pdf(data, filename):

    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("<b>Food Safety Audit Report</b>", styles["Title"]))
    elements.append(Spacer(1, 0.4 * inch))

    info = [
        ["Restaurant", data["restaurant_number"]],
        ["Manager", data["manager_name"]],
        ["Date", data["date"]],
        ["Score", f'{data["percentage"]}%'],
        ["Result", data["result"]],
    ]

    table = Table(info, colWidths=[2 * inch, 4 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))

    elements.append(table)
    doc.build(elements)
