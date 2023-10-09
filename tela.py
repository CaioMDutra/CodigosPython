import PySimpleGUI as sg

layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha', password_char='*')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')],

]

window = sg.Window('Login', layout=layout)

while True:
    event, values =  window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta = '@Caixj900'
        usuario_correto = 'Kylle'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login efetuado com sucesso! ')
        else:
            window['mensagem'].update('Login ou senha inválido! ')

