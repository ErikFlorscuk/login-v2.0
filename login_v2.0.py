import random 
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        sg.theme('DarkBlue')
        layout = [

            [sg.Text('Usuário'),sg.Input(key='usuario')],
            [sg.Text('Senha  '),sg.Input(key='senha',password_char='*')],
            [sg.Button('Cadastrar')],
            [sg.Button('Entrar')],
            [sg.Text('',key='mensagem')]
        ]
        # Declarar janela
        self.janela = sg.Window('Login v2.0',layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Cadastrar':
                nova_senha = self.salvar_senha(valores)
            if evento =='Entrar':
                login_correto = self.entrar_login(valores)

    def salvar_senha(self, valores):
        with open('logins.txt','a',newline='') as arquivo:
            arquivo.write(f"usuário: {valores['usuario']}, senha: {valores['senha']}\n")
        with open('logins.txt','r') as arquivo:
            logins = arquivo.readlines()
            for linha in logins:
                if "usuário" and "senha" in linha:
                    self.janela['mensagem'].update('Usuário cadastado com sucesso')
                
        print('Arquivo salvo') 

    def entrar_login(self, valores):
         with open('logins.txt','r') as arquivo:
            logins = arquivo.readlines()
            for linha in logins:
                if valores['usuario'] and valores['senha'] in linha:
                    self.janela['mensagem'].update('Login feito com sucesso')
                if valores['usuario'] and valores['senha'] not in linha:
                    self.janela['mensagem'].update('Login/senha incorreta ou usuário não cadastrado')


          
        
    


gen = PassGen()
gen.Iniciar()