import PyPDF2 as pyf
from pathlib import Path
import os

def getAllFunctionsName():
    path = os.getcwd() + '/functions/'
    functionsName = []

    for function in os.listdir(path):
        if function[-3:] == '.py':
            function = function.split('.')[0]
            functionsName.append(function)

    functionsName.remove('baseFunctions')

    return functionsName


def getAllFilesName():
    path = os.getcwd() + '/pdfs/'
    pdfsName = []

    for pdf in os.listdir(path):
        pdfsName.append(pdf)
    
    return pdfsName

def validationActionAndPdfName(action, pdfName):
    if not pdfName in getAllFilesName():
        return False
    if not action in getAllFunctionsName():
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