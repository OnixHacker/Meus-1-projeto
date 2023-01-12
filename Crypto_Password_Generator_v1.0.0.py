#Gerador de senhas codigo aberto, favor das os devidos creditos:
#Feito por Rafael Guedes
#version 1.0.0


import PySimpleGUI as sg
import pygame
import random
import string
import smtplib   
import email.message




sg.theme('Black')
sg.set_options(font='verdana 15')

pygame.mixer.init()
pygame.mixer.music.load('War_Crown.mp3')
pygame.mixer.music.play()

layout = [
        
        [sg.Image('pass.png')],
        [sg.Text('Maiúsculas: '), sg.Push(), sg.Input(size=15, key='-UP-')],
        [sg.Text('Minúsculas: '), sg.Push(), sg.Input(size=15, key='-LOW-')],
        [sg.Text('Dígitos: '), sg.Push(),sg.Input(size=15, key='-DIG-')],
        [sg.Text('Símbolos: '),sg.Push(), sg.Input(size=15, key='-SYM-')],
        [sg.Button('Gerar'), sg.Button('Sair')],
        [sg.Text('Senha  ==>> '),sg.Push(), sg.Multiline(size=15, no_scrollbar=True,
        disabled=True, key='-PASS-')],        
        [sg.Text('Enviar para email: '), sg.Push(), sg.Input(size=15, )],
        [sg.Button('sair e enviar')],
        
    ]

window = sg.Window('Crypto_Password_Generator_v1.1.0', icon='icopass.ico').layout(layout)

while True:
    event, values = window.read()
    if event == 'Sair' or  event == sg.WIN_CLOSED:        
        
        break

        

    if event == 'Gerar':
        try:
            u_upper = int(values['-UP-'])
            upper = random.sample(string.ascii_uppercase, u_upper)
            u_lower = int(values['-LOW-'])
            lower = random.sample(string.ascii_lowercase, u_lower)
            u_digits = int(values['-DIG-'])
            digits = random.sample(string.digits, u_digits)
            u_symbols = int(values['-SYM-'])
            symbols = random.sample(string.punctuation, u_symbols)
        

            total = upper+lower+digits+symbols
            total = random.sample(total, len(total))
            total = ''.join(total)
            window['-PASS-'].update(total)
        except ValueError:
            window['-PASS-'].update("Apenas números")
        
      
window.close()
""""
def enviar_email():
    corpo_email = 
  
    


msg = email.message.Message()
msg['Subject'] = 'Assunto'
msg['From'] = 'rafatattoox@gmail.com'
msg['To'] =  'rafatattoox@gmail.com'
password = 'fvgrarayqnqfhqic'
msg.add_header('Content-Type', 'text/html')
msg.set_payload('corpo_email')

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

s.login(msg['From'], password)
s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
sucesso = print('Email Enviado com sucesso!')


if sucesso:
    """

if values:
    poplayout = [

            [sg.popup_auto_close('email enviado com sucesso! ')],
            
    ]




            
