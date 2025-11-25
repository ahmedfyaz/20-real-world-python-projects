import pandas as pd
from fpdf import FPDF
import  glob
from pathlib import Path
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath,"Sheet 1")
    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_num = filename.split("-")[0]
    pdf.set_font(style="B",size=16,family="Times")
    pdf.cell(w=50,h=8,txt=f"Invoice nr{invoice_num}")
    pdf.output("PDFs/"+filename+".pdf")
