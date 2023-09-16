import sys
from functions.baseFunctions import validationActionAndPdfName, removeAllPagesFiles
from functions.GetOnePage import GetOnePage
from functions.GetAllPages import GetAllPages
from functions.GetFirstPage import GetFirstPage
from functions.GetLastPage import GetLastPage
from functions.GetPages import GetPages

action = sys.argv[1]
file = sys.argv[2]
pages = sys.argv[3:]

if validationActionAndPdfName(action, file):

    path = f'./pdfs/' + file

    match action:
        case 'GetAllPages':
            exec = GetAllPages()
            exec.execute(path)
        case 'GetOnePage':
            exec = GetOnePage()
            exec.execute(path, pages)
        case 'GetFirstPage':
            exec = GetFirstPage()
            exec.execute(path)
        case 'GetLastPage':
            exec = GetLastPage()
            exec.execute(path)
        case 'GetPages':
            exec = GetPages()
            exec.execute(path, pages)
else:
    print('Some of the parameters are wrong')