import io

from reportlab.pdfgen import canvas
# from reportlab.pdfbase import pdfmetrics

import io
from reportlab.pdfgen import canvas

class PdfService:
    def generate_car_pdf(car) -> bytes:
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.setFont('Helvetica-Bold', 16)
        p.drawString(100, 750, 'Car Details')
        p.setFont('Helvetica', 12)
        p.drawString(100, 725, f"Name: {car.name}")
        p.drawString(100, 700, f"Year: {car.year}")
        p.drawString(100, 675, f"Description: {car.description}")
        p.drawString(100, 650, f"Sold: {'Yes' if car.sold else 'No'}")
        # p.drawString(100, 625, f"Owner: {car.user.email}")
        p.save()

        buffer.seek(0)
        pdf_file = buffer.getvalue()
        buffer.close()
        return pdf_file