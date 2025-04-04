import os

os.system("cls || clear")


def media(n1, n2):
    return (n1 + n2) / 2

n1 = float(input("Digite o primeiro numero:"    ))
n2 = float(input("Digite o segundo numero:"    ))

mediana = media(n1,n2)

print(f"Media:{mediana}")