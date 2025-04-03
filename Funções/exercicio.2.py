import os

os.system("Clear")



def verificar_paridade():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

# Chamando a função
verificar_paridade()