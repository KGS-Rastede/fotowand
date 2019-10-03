# simple_demo.py
 
from fpdf import FPDF
 
# L = Landscape, P = Portrait
pdf = FPDF(orientation='L', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Test der Fotowand", ln=1, align="C") # C: Center
pdf.output("fotowand.pdf")

