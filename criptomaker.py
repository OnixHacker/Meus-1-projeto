#Rafael Guedes 
#github.com/OniXHacker

import PySimpleGUI as sg



sg.theme('black')
menu_def = [['&Menu',['&Abrir', '&Salvar', '&Sobre...', '&Como usar',  '&Sair']],
            ['&Ajude-me', '&Doação'], ]

layout = [
    [sg.Menu(menu_def, tearoff=False, key='-MENU BAR-')],
    [sg.Image('crypto.png')],
    [sg.Text('Digite o texto ser Criptográfado(ou Descriptográfado)abaixo')],
    [sg.Output(size=(66,25))], 
    [sg.Button('Criptográfar'), sg.Button('Descriptográfar')],
    [sg.Text("Todos direitos reservados®,feito por Rafael Guedes")],      
 ]  
window = sg.Window('Crypto All Max®', icon='icopass.ico').layout(layout)
while True:
    event, values = window.read()
    if event == 'Sair' or  event == sg.WIN_CLOSED:    
        break    
        
def cripto(frase):
    tradutor = " "
    if event == 'Criptográfar':
   
        for letra in frase:
            if letra in "Aa":
                tradutor = tradutor + "{"
            elif letra in "Ff":
                tradutor = tradutor + "5"  
            elif letra in "Ee":
                tradutor = tradutor + "#"   
            elif letra in "Ll":
                tradutor = tradutor + "n"   
            elif letra in "Gg":
                tradutor = tradutor + "$"   
            elif letra in "Dd":
                tradutor = tradutor + ")"   
            elif letra in "Uu":
                tradutor = tradutor + "/"   
            elif letra in "Rr":
                tradutor = tradutor + "+"
            elif letra in "Nn":
                tradutor = tradutor + "z"
            elif letra in "Ww":
                tradutor = tradutor + "."
            elif letra in "Zz":
                tradutor = tradutor + "^"
            elif letra in "6":
                tradutor = tradutor + "0"
            elif letra in "Cc":
                tradutor = tradutor + "~"
            elif letra in "Tt":
                tradutor = tradutor + "|"
            elif letra in "\\":
                tradutor = tradutor + ":"
            elif letra in "Bb":
                tradutor = tradutor + ":)"
            elif letra in "Hh":
                tradutor = tradutor + "*"
            elif letra in "wW":
                tradutor = tradutor + "%"

            else:
                tradutor = tradutor + letra

    return tradutor

print(cripto(input("Digite sua frase: ")))

