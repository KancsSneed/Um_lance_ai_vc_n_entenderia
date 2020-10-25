from PySimpleGUI import PySimpleGUI as sg 

#Layout
sg.theme('DarkPurple1')
layout = [
    [sg.Text('Nome'), sg.Input(key='name')],
    [sg.Text('Senha'), sg.Input(key='password', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Confirmado')]
]
#Janela
janela = sg.Window('Tela de Login', layout)
#Evento
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Confirmado':
        #Salvar os dados e fechar a interface
        sg.WINDOW_CLOSED()