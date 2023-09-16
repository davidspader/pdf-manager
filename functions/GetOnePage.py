from functions.baseFunctions import separeteAllPages, writePDF

class GetOnePage:

    def execute(self, path, page):
        page = int(page[0]) - 1
        try:
            allPages = separeteAllPages(path)
            newPDF = allPages[page]
            writePDF(newPDF, path)
        except:
            print('Some of the parameters are wrong')



