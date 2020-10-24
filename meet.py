import os
from datetime import date
from datetime import datetime
from time import sleep
from pathlib import Path

hora = 3600

    #execução do programa

#1° etapa - configurando o log, caso o usuário não tenha logado
fileName = r"log.txt"
fileObj = Path(fileName)
fileObj.is_file()

#Caso o arquivo exista o programa irá ler
if fileObj.is_file() == True:
    with open('log.txt', 'r') as arquivo:
        for valor in arquivo:
            log = valor
#Caso não exista irá criar
else:
    log = input("O que é para ser salvo?")
    with open('log.txt', 'w') as arquivo:
        arquivo.write(str(log))


# 2° Etapa - Aulas

#Funções da semana
def segunda():
    if now.hour == 16:
        os.startfile(log)
        quit()
def terca():
    if now.hour == 18:
        os.startfile(log)
        quit()
def quarta():
    if now.hour == 10:
        os.startfile(log)
        sleep(hora * 6)
    elif now.hour == 16:
        os.startfile(log)
        quit()
def quinta():
    if now.hour == 9:
        os.startfile(log)
        sleep(hora * 6)
    elif now.hour == 15:
        os.startfile(log)
        quit()
def sexta():
    if now.hour == 10:
        os.startfile(log)
        sleep(hora * 3)
    elif now.hour == 13:
        os.startfile(log)
        sleep(hora * 2)
    elif now.hour == 15:
        os.startfile(log)
        quit()

while True:
    now = datetime.now()
    data = date(now.year, now.month, now.day)
#segunda
    if data.isoweekday() == 1:
        segunda()  
#terça
    elif data.isoweekday() == 2:
        terca()
#quarta
    elif data.isoweekday() == 3:
        quarta()
#quinta
    elif data.isoweekday() == 4:
        quinta()
#sexta
    elif data.isoweekday() == 5:
        sexta()
    elif data.isoweekday() == 6 or 7:
        print("É feriado danado, vai dormir.")
        quit()
    sleep(120)


