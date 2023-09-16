from functions.baseFunctions import separeteAllPages, writePDF

class GetLastPage:

    def execute(self, path):
        try:
            allPages = separeteAllPages(path)
            newPDF = allPages[-1]
            writePDF(newPDF, path)
        except:
            print('Some of the parameters are wrong')