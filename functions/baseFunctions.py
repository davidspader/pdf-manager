import PyPDF2 as pyf
from pathlib import Path
from functions.getAllFunctionsName import functionsName, pdfsName

def validationActionAndPdfName(action, pdfName):
    if not pdfName in pdfsName:
        return False
    if not action in functionsName:
        return False
    return True

def separeteAllPages(file):
    allPages = []

    pdf = pyf.PdfReader(file)

    for pagina in pdf.pages:
        newPDF = pyf.PdfWriter()
        newPDF.add_page(pagina)
        allPages.append(newPDF)

    return allPages

def writePDF(file, path):
    path = path.replace('.pdf', '-new.pdf')
    with Path(path).open(mode='wb') as finalPDF:
        file.write(finalPDF)
