import os

os.system("cls || Clear")



def verificar_paridade():
    numero = int(input("Digite um número: "))
    if numero >= 0:
        print(f"O número {numero} é positivo.")
    else:
        print(f"O número {numero} é negativo.")

# Chamando a função
verificar_paridade()