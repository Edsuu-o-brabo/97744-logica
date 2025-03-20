import os  

os.system("clear")

login_correto = "usuario123"
senha_correta = "senha456"
while True:
       
        login = input("Digite seu login: ")

        
        senha = input("Digite sua senha: ")

        if login == login_correto and senha == senha_correta:
            print("Login e senha corretos! Acesso concedido.")
            break
        else:
            print("Login ou senha incorretos. Tente novamente.")
