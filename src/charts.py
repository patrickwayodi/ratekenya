import json
import io

from datetime import date
from datetime import timedelta

from reportlab.graphics import renderPDF
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen import canvas


def annual_totals(rating_list_stats):

    with open(rating_list_stats, "r") as json_file:
        rating_stats = json.load(json_file)

    totals = (
        rating_stats["2015-12-01"]["Total Kenya"],
        rating_stats["2016-12-01"]["Total Kenya"],
        rating_stats["2017-12-01"]["Total Kenya"],
        rating_stats["2018-12-01"]["Total Kenya"],
        rating_stats["2019-12-01"]["Total Kenya"],
        rating_stats["2020-12-01"]["Total Kenya"],
        rating_stats["2021-12-01"]["Total Kenya"],
        rating_stats["2022-12-01"]["Total Kenya"],
        rating_stats["2023-12-01"]["Total Kenya"],
        rating_stats["2024-12-01"]["Total Kenya"],
        rating_stats["2025-12-01"]["Total Kenya"]
    )

    output_file = "rating-stats.pdf"

    # Create the PDF object
    c = canvas.Canvas(output_file)

    drawing = Drawing(500, 500)
    data = [totals,]
    lc = HorizontalLineChart()
    lc.x = 50
    lc.y = 50
    lc.height = 400
    lc.width = 400
    lc.data = data
    lc.joinedLines = 1
    catNames = "2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025".split(" ")
    lc.categoryAxis.categoryNames = catNames
    lc.categoryAxis.labels.boxAnchor = 'n'
    lc.valueAxis.valueMin = 0
    lc.valueAxis.valueMax = 1600
    lc.valueAxis.valueStep = 200
    lc.lines[0].strokeWidth = 2
    lc.lines[1].strokeWidth = 1.5
    drawing.add(lc)

    # renderPDF.drawToFile(drawing, 'example1.pdf', 'My First Drawing')
    drawing.drawOn(c,50,250)

    # Draw things on the PDF. Here's where the PDF generation happens.
    c.setFont("Helvetica-Bold", 20)
    c.drawString(147,750,"Rated Chess Players in Kenya")
    c.setFont("Helvetica", 16)
    c.drawString(162,725,"(December 2015 to December 2025)")
    c.setFont("Helvetica", 16)
    c.drawString(285,260,"Year")
    c.rotate(90)
    c.drawString(480,-60,"Players")  # Note the "-" sign of "60"

    # Close the PDF object cleanly, and we're done.
    c.showPage
    c.save()

    return output_file


if __name__ == '__main__':

    print("\nCharts")
    print("======\n")

    print("\nAnnual Trends:", annual_totals("rating-list-stats.json"))

    print("\n\n")

