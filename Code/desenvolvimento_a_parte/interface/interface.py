from PySimpleGUI import PySimpleGUI as sg 
from pathlib import Path
import os
 


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
        janela = sg.Window('Configuração de dependencias').layout(layout)
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

fileName = r"log.txt"
fileObj = Path(fileName)
fileObj.is_file()

if fileObj.is_file() == True:
    with open('log.txt', 'r') as arquivo:
        log = arquivo.readline()
        time = arquivo.readline()
        sound = arquivo.readline()
        print(log, time, sound)
else:
    with open('log.txt', 'w') as arquivo:
        inteface = tela()
        inteface.resgistrar_log()



