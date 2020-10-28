import pyautogui
from time import sleep
from pathlib import Path

#while True:
    #sleep(5)
    #arquivo = open(r'local.txt', 'w')
    #arquivo.write(str(pyautogui.position()))
    #pyautogui.click(pyautogui.position())
    #break
#sleep(5)
#pyautogui.click(arquivo.read(r'local.txt', 'r'))

fileName = r"local.txt"
fileObj = Path(fileName)

while True:
    if fileObj.is_file() == True:
        with open('local.txt', 'r') as arquivo:
            for valor in arquivo:
                coordenada_x = valor
                print(range(coordenada_x))
                #pyautogui.click(pyautogui.position(valor))
        break
    else:
        with open('local.txt', 'w') as arquivo:
            sleep(5)
            arquivo.write(str(pyautogui.position()))
        break