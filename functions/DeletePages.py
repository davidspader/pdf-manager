from functions.baseFunctions import removeAllPagesFiles, writePDF, validatePages, getAllFilesName
from functions.GetAllPages import GetAllPages
import PyPDF2 as pyf

class DeletePages:

    def execute(self, path, pages):
        try:
            pages = validatePages(pages)
            
            exec = GetAllPages()
            exec.execute(path)

            newPDF = pyf.PdfWriter()

            files = getAllFilesName(True)

            for file in files:
                fileNumber = file[:-4].split('-')
                if not fileNumber[1] in pages:
                    filePath = path.replace("/pdfs/", f"/pdfs/allPages/")
                    fileName = filePath.replace(".pdf", f"-{fileNumber[1]}.pdf")

                    file = pyf.PdfReader(fileName)
                    page = file.pages[0]
                    newPDF.add_page(page)

            writePDF(newPDF, path)
            removeAllPagesFiles()
        except:
            print('Some of the parameters are wrong')