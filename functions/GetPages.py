from functions.baseFunctions import removeAllPagesFiles, writePDF, validatePages
from functions.GetAllPages import GetAllPages
import PyPDF2 as pyf

class GetPages:

    def execute(self, path, pages):
        try:
            pages = validatePages(pages)
            
            exec = GetAllPages()
            exec.execute(path)

            newPDF = pyf.PdfWriter()

            for num_page in pages:
                filePath = path.replace("/pdfs/", "/pdfs/allPages/")
                fileName = filePath.replace(".pdf", f"-{num_page}.pdf")
                
                file = pyf.PdfReader(fileName)
                page = file.pages[0]
                newPDF.add_page(page)

            writePDF(newPDF, path)
            removeAllPagesFiles()
        except:
            print('Some of the parameters are wrong')