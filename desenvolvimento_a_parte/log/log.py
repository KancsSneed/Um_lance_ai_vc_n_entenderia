from pathlib import Path
 
log = 'Pois é irmão'

fileName = r"C:\Users\luisk\Documents\MeuProjetos\Um_lance_ai_vc_n_entenderia\desenvolvimento_a_parte\log\log.txt"
fileObj = Path(fileName)
fileObj.is_file()

if fileObj.is_file() == True:
    with open('log.txt', 'r') as arquivo:
        for valor in arquivo:
            print(valor)
else:
    with open('log.txt', 'w') as arquivo:
        arquivo.write(str(log))