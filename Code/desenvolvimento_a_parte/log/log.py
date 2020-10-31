from pathlib import Path

fileName = r"log.txt"
fileObj = Path(fileName)
fileObj.is_file()

valor = [1,2,3,4,5]
#if fileObj.is_file() == True:
#    with open('log.txt', 'r') as arquivo:
#        for valor in arquivo:
#            print(valor)
#else:
with open('log.txt', 'a') as arquivo:
    for var in valor:
        arquivo.write(str(var)+'\n')