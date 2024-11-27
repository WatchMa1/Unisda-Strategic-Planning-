from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_pdf(data, filename="output.pdf"):
    doc = SimpleDocTemplate(filename)
    elements = []

    # Header Row
    table_data = [["Themes", "Objectives", "KPIs", "Main Activities", "Sub-Activities", "Score Q1", "Explanation"]]
    
    for theme in data:
        for obj_data in theme['objectives']:
            for kpi_data in obj_data['kpis']:
                for main_activity_data in kpi_data['main_activities']:
                    for activity in main_activity_data['activities']:
                        row = [
                            theme['theme'].theme_name if theme['theme_row_span'] > 0 else '',
                            obj_data['objective'].objective_name if obj_data['objective_row_span'] > 0 else '',
                            kpi_data['kpi'].name if kpi_data['kpi_row_span'] > 0 else '',
                            main_activity_data['main_activity'].name if main_activity_data['activities'] else '',
                            activity.name,
                            "",  # Score
                            ""   # Explanation
                        ]
                        table_data.append(row)
    
    # Add Table Styling
    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # Build PDF
    doc.build(elements)
    return filename
