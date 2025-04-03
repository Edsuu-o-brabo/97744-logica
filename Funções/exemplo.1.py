import os 

os.system("Clear")


def saudacao(nome):
    print(f"Olá {nome}!Bem vindo ao curso de DS!")          

#crie uma função com o nome: Diciplina que receba o nome de 
# uma diciplina do curso de DS.
# mostre o texto:A diciplina *** faz parte do curso de DS

def diciplina(nome_diciplinha):
    print(f"A diciplina {nome_diciplinha} que faz parte do curso de DS")

nome = input("Digite o seu nome:  ")
nome_diciplina = input("Digite o Nome da Matéria:  ")


saudacao(nome)          
diciplina(nome_diciplina)
