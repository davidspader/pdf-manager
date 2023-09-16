import sys
from functions.baseFunctions import validationActionAndPdfName
from functions.GetOnePage import GetOnePage
from functions.GetAllPages import GetAllPages

action = sys.argv[1]
file = sys.argv[2]
pages = sys.argv[3:]

if validationActionAndPdfName(action, file):

    path = f'./pdfs/' + file

    match action:
        case 'GetOnePage':
            exec = GetOnePage()
            exec.execute(path, pages)
        case 'GetAllPages':
            exec = GetAllPages()
            exec.execute(path)
else:
    print('Some of the parameters are wrong')