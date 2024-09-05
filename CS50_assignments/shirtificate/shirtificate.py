from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", "B", 40)
pdf.cell(0, 60, "CS50 Shirtificate", align = "C")
pdf.image("shirtificate.png", x=0, y=65)
pdf.set_font("Times", "", 30)
pdf.set_text_color(255, 255, 255)
pdf.text(x=50, y=150, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")