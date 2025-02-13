import os

# Limpa o terminal.
os.system("clear")

#solicitar dados do usuário.
nome = input("Digite seu nome: ")
idade = int(input ("Digite sua idade: "))
altura = float(input("Digite sua altura: "))


#exibindo dados.
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")