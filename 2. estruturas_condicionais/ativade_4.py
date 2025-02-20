import os

os.system("clear") # Limpa o Terminal

login_cadastrado = "edson555"
senha_cadastrada = "12345"

login = input("Digite seu login:  ")
senha =  input("Digite sua senha:  ")



if login_cadastrado == login and senha_cadastrada == senha:
   print("Bem vindo!") 
else: 
   print("login ou senha inválidos!")