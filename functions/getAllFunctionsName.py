import os

path = os.getcwd() + '/functions/'
functionsName = []

for function in os.listdir(path):
    if function[-3:] == '.py':
        function = function.split('.')[0]
        functionsName.append(function)

functionsName.remove('getAllFunctionsName')

path = os.getcwd() + '/pdfs/'
pdfsName = []

for pdf in os.listdir(path):
    pdfsName.append(pdf)