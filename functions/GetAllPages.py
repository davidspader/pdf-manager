from functions.baseFunctions import separeteAllPages, writePDF

class GetAllPages:

    def execute(self, path):
        try:
            allPages = separeteAllPages(path)
            
            for i, page in enumerate(allPages):
                newPath = path.replace(".pdf", f"-{i + 1}.pdf")
                writePDF(page, newPath)
        except:
            print('Some of the parameters are wrong')