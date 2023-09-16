import sys
from functions.baseFunctions import validationActionAndPdfName
from functions.GetOnePage import GetOnePage

action = sys.argv[1]
file = sys.argv[2]
pages = sys.argv[3:]

if validationActionAndPdfName(action, file):

    file = f'./pdfs/' + file

    match action:
        case 'GetOnePage':
            exec = GetOnePage()
            exec.execute(file, pages)
    
else:
    print('Some of the parameters are wrong')