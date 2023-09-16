import sys
import PyPDF2 as pyf
from functions.validationActionAndPdfName import validationActionAndPdfName
from functions.Test import Test
from functions.Blabla import Blabla

action = sys.argv[1]
filePath = sys.argv[2]

if validationActionAndPdfName(action, filePath):
    print('code here :D')
else:
    print('Some of the parameters are wrong')