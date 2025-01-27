from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import datetime


class PDF(FPDF):
    def header(self):
        self.set_y(5)
        self.set_font("helvetica", "", 10)
        w = self.w
        l_margin = self.l_margin
        r_margin = self.r_margin
        width = (w - l_margin - r_margin)
        self.cell(width / 3, 10, "Prüfbericht", border=False, align="L")
        self.cell(width / 3, 10, "Prüfbericht", border=False, align="C")
        self.cell(width / 3, 10, "Prüfbericht", border=False, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        w = self.w
        l_margin = self.l_margin
        r_margin = self.r_margin
        width = (w - l_margin - r_margin)
        exam_date = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
        self.set_font("helvetica", "", 10)
        self.cell(width / 2, 10, f"Seite {self.page_no()} von {self.pages_count}", border=False, align="L")
        self.cell(width / 2, 10, f"{exam_date}", border=False, align="R")


pdf = PDF("P", "mm", "A4")
pdf.set_title("Prüfbericht - Nachname Vorname")
pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_page()
pdf.set_font("helvetica", "B", 16)

pdf.cell(0, 10, "Prüfbericht nach ÖNORM M 7861-6:2009", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(5)

pdf.set_font("helvetica", "U", 12)
pdf.cell(0, 10, "Erzeugnisdaten:", align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.output("Pruefbericht_Nachname_Vorname.pdf")
