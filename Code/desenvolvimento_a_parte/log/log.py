from pathlib import Path

fileName = r"log.txt"
fileObj = Path(fileName)
fileObj.is_file()

if fileObj.is_file() == True:
    with open('log.txt', 'r') as arquivo:
        for valor in arquivo:
            print(valor)
else:
    with open('log.txt', 'w') as arquivo:
        arquivo.write(str(log))