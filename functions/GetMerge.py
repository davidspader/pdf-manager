import PyPDF2 as pyf
from functions.baseFunctions import writePDF

class GetMerge:

    def execute(self, path, path2):
        try:
            path2 = './pdfs/' + path2[0]
            newPDF = pyf.PdfMerger()

            newPDF.append(path)
            newPDF.append(path2)

            writePDF(newPDF, path)
        except:
            print('Some of the parameters are wrong')