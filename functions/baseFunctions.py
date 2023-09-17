import PyPDF2 as pyf
from pathlib import Path
import os

def getAllFunctionsName():
    path = os.getcwd() + r'/functions/'
    functionsName = []

    for function in os.listdir(path):
        if function[-3:] == '.py':
            function = function.split('.')[0]
            functionsName.append(function)

    functionsName.remove('baseFunctions')

    return functionsName


def getAllFilesName(allPages=False):
    if not allPages:
        path = os.getcwd() + r'/pdfs/'
    else:
        path = os.getcwd() + r'/pdfs/allPages/'

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

def writePDF(file, path, allPages=False):
    if not allPages:
        path = path.replace('.pdf', '-new.pdf')
    else:
        path = path.replace(r'/pdfs/', '/pdfs/allPages/')

    with Path(path).open(mode='wb') as finalPDF:
        file.write(finalPDF)

def removeAllPagesFiles():
    path = os.getcwd() + r'/pdfs/allPages/'
    fileNames = getAllFilesName(True)

    for fileName in fileNames:
        os.remove(path + fileName)
    