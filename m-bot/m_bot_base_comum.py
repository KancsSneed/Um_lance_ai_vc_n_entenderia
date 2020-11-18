from pygame import mixer
import os
from datetime import date
from datetime import datetime
from time import sleep
from pathlib import Path
from PySimpleGUI import PySimpleGUI as sg
import pyautogui
from playsound import playsound


hora = 3600

    #execução do programa
#depedencias
        #1° etapa - configurando o log, caso o usuário não tenha logado
    #Interface
class tela:
    def __init__(self):
        sg.theme('DarkPurple1')
        #Layout's
        layout = [
            [sg.Text('Cole o URL da reunião já logado com a conta etepd.com na caixa de texto abaixo.')],
            [sg.Text('URL:'), sg.Input(key='log')],
            [sg.Text('De quanto em quanto tempo o programa deve verificar?')],
            [sg.Radio('2 Minutos','calibragem', key='doisminutos'), sg.Radio('4 Minutos','calibragem', key='quatrominutos')],
            [sg.Text('Configuração de alerta:')],
            [sg.Radio('Yamete','mp3', key='yamete'), sg.Radio('Sonic','mp3', key='sonic')],
            [sg.Button('Confirmar')]
        ]
        #Janelas
        janela = sg.Window('Tela de Login').layout(layout)
        #Dados
        self.Button, self.values = janela.read()


    def resgistrar_log(self):
        if self.values['doisminutos'] == True:
            time = '120'
        else:
            time = '240'
        if self.values['sonic'] == True:
            sound = 'Sonic.mp3'
        elif self.values['yamete'] == True:
            sound = 'Yamete.mp3'
        valor = [self.values['log'], time, sound]
        with open('dependencias/log.txt', 'a') as arquivo:
            for var in valor:
                arquivo.write(str(var) + '\n')

#Registro de log
fileName = r"dependencias/log.txt"
fileObj = Path(fileName)
fileObj.is_file()

if fileObj.is_file() == True:
    with open('dependencias/log.txt', 'r') as arquivo:
        log = arquivo.readline()
        time = arquivo.readline()
        sound = arquivo.readline()
else:
    with open('dependencias/log.txt', 'w') as arquivo:
        inteface = tela()
        inteface.resgistrar_log()

# 2° Etapa - Aulas
#função click
def click():
    while True:
        sleep(1)
        if pyautogui.locateOnScreen("dependencias/dispensar.py", grayscale=True, confidence = 0.8)  != None:
            pyautogui.click('dependencias/dispensar.py')
            sleep(1)
            pyautogui.click('dependencias/entrar.py')
            break
#Funções Diversas
def reproduzindo_sound():
    if sound != None:
        playsound(f"dependencias\sounds\{sound}")

#Funções da semana
def segunda():
    print("Aula presencial!")
    quit()
def terca():
    if now.hour == 9:
        os.startfile(log)
        click()
        sleep(hora * 6)
    elif now.hour == 15:
        os.startfile(log)
        click()
        quit()
def quarta():
    if now.hour == 10:
        os.startfile(log)
        click()
        sleep(hora * 6)
    elif now.hour == 16:
        os.startfile(log)
        click()
        quit()
def quinta():
    if now.hour == 9:
        os.startfile(log)
        click()
        sleep(hora)
    elif now.hour == 10:
        os.startfile(log)
        click()
        sleep(hora * 3)
    elif now.hour == 13:
        os.startfile(log)
        click()
        sleep(hora * 3)
    elif now.hour == 16:
        os.startfile(log)
        click()    
        quit()
def sexta():
    if now.hour == 10:
        os.startfile(log)
        click()
        sleep(hora * 3)
    elif now.hour == 13:
        os.startfile(log)
        click()
        sleep(hora * 2)
    elif now.hour == 15:
        os.startfile(log)
        click()
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
    sleep(int(time))


