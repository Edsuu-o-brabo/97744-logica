import os

os.system("cls || clear")


def somar(n1, n2):
    calcular = n1 + n2
    return calcular

def subtrair(n1, n2):
    calcular = n1 - n2
    return calcular

def divisao(n1, n2):
    calcular = n1 / n2
    return calcular
    
def multiplicar(n1, n2):
    calcular = n1 * n2
    return calcular


n1 = int(input("Digite o primeiro numero:"    ))
n2 = int(input("Digite o segundo numero:"    ))

soma = somar(n1,n2)
subtracao = subtrair(n1, n2)
dividir = divisao(n1 , n2)
multiplicacao = multiplicar(n1 , n2)

print()
print("=====Esses resultado======")
print(f"Soma:{soma}")
print(f"Subtração :{subtracao}")
print(f"Divisão:{dividir}")
print(f"Divisão:{multiplicacao}")
