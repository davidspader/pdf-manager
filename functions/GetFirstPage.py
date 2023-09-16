from functions.baseFunctions import separeteAllPages, writePDF

class GetFirstPage:

    def execute(self, path):
        page = 0
        try:
            allPages = separeteAllPages(path)
            newPDF = allPages[page]
            writePDF(newPDF, path)
        except:
            print('Some of the parameters are wrong')