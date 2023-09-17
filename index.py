import sys
from functions.baseFunctions import validationActionAndPdfName, removeAllPagesFiles
from functions.GetOnePage import GetOnePage
from functions.GetAllPages import GetAllPages
from functions.GetFirstPage import GetFirstPage
from functions.GetLastPage import GetLastPage
from functions.GetPages import GetPages
from functions.GetMerge import GetMerge
from functions.GetRotatePages import GetRotatePages
from functions.DeletePages import DeletePages

action = sys.argv[1]
file = sys.argv[2]
thirdParameter = sys.argv[3:]

if validationActionAndPdfName(action, file):

    path = r'./pdfs/' + file

    match action:
        case 'GetAllPages':
            exec = GetAllPages()
            exec.execute(path)
        case 'GetOnePage':
            exec = GetOnePage()
            exec.execute(path, thirdParameter)
        case 'GetFirstPage':
            exec = GetFirstPage()
            exec.execute(path)
        case 'GetLastPage':
            exec = GetLastPage()
            exec.execute(path)
        case 'GetPages':
            exec = GetPages()
            exec.execute(path, thirdParameter)
        case 'RemoveAllPagesFiles':
            removeAllPagesFiles()
        case 'GetMerge':
            exec = GetMerge()
            exec.execute(path, thirdParameter)
        case 'GetRotatePages':
            exec = GetRotatePages()
            exec.execute(path, thirdParameter)
        case 'DeletePages':
            exec = DeletePages()
            exec.execute(path, thirdParameter)
    print('successfully executed')
else:
    print(validationActionAndPdfName(action, file))
    print('Some of the parameters are wrong')