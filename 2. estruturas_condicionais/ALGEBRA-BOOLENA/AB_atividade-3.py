import os
os.system("clear")


n1=int(input("Digite o primeiro numero: "))
operacao = input("Digite a operaçãp desejada: ")
n2=int(input("Digite o segundo numero: "))

import os
os.system("clear")

match operacao:
    case "+": 
        resultado = n1 + n2 
    case "-": 
        resultado = n1 - n2
    case "/":
        resultado = n1 / n2
    case "*": 
        resultado = n1 * n2
    case _:
        print("Opção inválida. ")        

print()
print(f"Primeiro numero: {n1}")
print(f"Operação: {operacao}")
print(f"Segundo numero:  numero: {n2}")
print(f"Primeiro numero: {n1}")
print(f"Resultado: {resultado}")
