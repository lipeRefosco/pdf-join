"""Module provaded to define the return type of open_all_files funcition"""
from PyPDF2 import PdfReader, PdfWriter

def join(user_input_parsed):
    """Script to Command Join"""
    all_pdf = [PdfReader(file) for file in user_input_parsed.get("inputs")]
    new_pdf = PdfWriter()

    for pdf in all_pdf:
        new_pdf.append(pdf)

    new_pdf.write(user_input_parsed.get("output"))
    new_pdf.close()
