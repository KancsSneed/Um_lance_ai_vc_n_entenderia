from PySimpleGUI import PySimpleGUI as sg 

#Layout
sg.theme('DarkPurple1')
layout = [
    #[sg.Text('Nome'), sg.Input(key='name')],
    #[sg.Text('Senha'), sg.Input(key='password', password_char='*')],
    #[sg.Checkbox('Salvar o login?')],
    #[sg.Button('Confirmado')]
    [sg.Text('Cole o URL da reunião já logado com a conta etepd.com na caixa de texto abaixo.')],
    [sg.Text('URL:'), sg.Input(key='log')],
    [sg.Button('Confirmar')]
]
#Janela
janela = sg.Window('Tela de Login', layout)
#Evento
while True:
    evento, valor = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Confirmar':
        #Salvar os dados e fechar a interface
        break