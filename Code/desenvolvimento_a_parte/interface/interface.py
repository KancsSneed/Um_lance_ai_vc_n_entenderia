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
        valor = [self.values['log'], time]
        with open('dependencias/log.txt', 'a') as arquivo:
            for var in valor:
                arquivo.write(str(var) + '\n')

#Dependencias
dir = r'./dependencias'
pasta = Path(dir)
if pasta.is_dir() == False:
    os.mkdir(dir)
    os.mkdir(dir+'/img')

fileName = r"log.txt"
fileObj = Path(fileName)
fileObj.is_file()

if fileObj.is_file() == True:
    with open('dependencias/log.txt', 'r') as arquivo:
        log = arquivo.readline()
        time = arquivo.readline()
        print(log, time)
else:
    with open('dependencias/log.txt', 'w') as arquivo:
        inteface = tela()
        inteface.resgistrar_log()



