import PyPDF2 as pyf
from functions.baseFunctions import writePDF

class GetRotatePages:

    def execute(self, path, degrees):
        try:
            file = pyf.PdfReader(path)

            newPDF = pyf.PdfWriter()
            for num_page in file.pages:
                num_page.rotate(int(degrees[0]))
                newPDF.add_page(num_page)

            writePDF(newPDF, path)
        except:
            print('Some of the parameters are wrong')