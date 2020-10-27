import os
from datetime import date
from datetime import datetime
from time import sleep
from pathlib import Path
from PySimpleGUI import PySimpleGUI as sg
import pyautogui

hora = 3600
log = str
    #execução do programa

        #1° etapa - configurando o log, caso o usuário não tenha logado

    #Interface
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
    #Layout
    sg.theme('DarkPurple1')
    layout = [
        [sg.Text('Cole o URL da reunião já logado com a conta etepd.com na caixa de texto abaixo.')],
        [sg.Text('URL:'), sg.Input(key='log')],
        [sg.Button('Confirmar')]
    ]
    #Janela
    janela = sg.Window('Configuração de log', layout)
    #Evento
    while True:
        evento, valor = janela.read()
        if evento == sg.WINDOW_CLOSED:
            break
        if evento == 'Confirmar':
            log = valor['log']
            break
    with open('log.txt', 'w') as arquivo:
        arquivo.write(log)

# 2° Etapa - Aulas

#Funções da semana
def segunda():
    if now.hour == 16:
        os.startfile(log)
        sleep(5)
        pyautogui.click(875, 501)
        sleep(4)
        pyautogui.click(970, 429)
        quit()
def terca():
    if now.hour == 15:
        os.startfile(log)
        sleep(5)
        pyautogui.click(875, 501)
        sleep(4)
        pyautogui.click(970, 429)
        quit()
def quarta():
    if now.hour == 10:
        os.startfile(log)
        sleep(5)
        pyautogui.click(875, 501)
        sleep(4)
        pyautogui.click(970, 429)
        sleep(hora * 6)
    elif now.hour == 16:
        os.startfile(log)
        sleep(5)
        pyautogui.click(875, 501)
        sleep(4)
        pyautogui.click(970, 429)
        quit()
def quinta():
    if now.hour == 9:
        os.startfile(log)
        sleep(5)
        pyautogui.click(875, 501)
        sleep(4)
        pyautogui.click(970, 429)
        sleep(hora * 6)
    elif now.hour == 15:
        os.startfile(log)
        sleep(5)
        pyautogui.click(875, 501)
        sleep(4)
        pyautogui.click(970, 429)
        quit()
def sexta():
    if now.hour == 10:
        os.startfile(log)
        sleep(5)
        pyautogui.click(875, 501)
        sleep(4)
        pyautogui.click(970, 429)
        sleep(hora * 3)
    elif now.hour == 13:
        os.startfile(log)
        sleep(5)
        pyautogui.click(875, 501)
        sleep(4)
        pyautogui.click(970, 429)
        sleep(hora * 2)
    elif now.hour == 15:
        os.startfile(log)
        sleep(5)
        pyautogui.click(875, 501)
        sleep(4)
        pyautogui.click(970, 429)
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
    sleep(60)


