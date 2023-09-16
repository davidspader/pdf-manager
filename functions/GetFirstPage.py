from functions.baseFunctions import separeteAllPages, writePDF

class GetFirstPage:

    def execute(self, path):
        try:
            allPages = separeteAllPages(path)
            newPDF = allPages[0]
            writePDF(newPDF, path)
        except:
            print('Some of the parameters are wrong')