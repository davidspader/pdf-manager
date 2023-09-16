from functions.getAllFunctionsName import functionsName, pdfsName

def validationActionAndPdfName(action, pdfName):
    if not pdfName in pdfsName:
        return False
    if not action in functionsName:
        return False
    return True