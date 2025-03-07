import os
os.system("clear")

cor = input("Digite a cor do CD: ").lower()

if cor == "vermelho":
    preco = 20.00
elif cor == "azul":
    preco = 25.00
elif cor == "verde":
    preco = 30.00
elif cor == "amarelo":
    preco = 35.00
else:
    preco = "Cor inválida"

print(f"O preço do CD é: {preco}")