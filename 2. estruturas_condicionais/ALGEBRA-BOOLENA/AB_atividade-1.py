import os

os.system("clear") 

numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))
numero_3 = int(input("Digite o terceiro numero: "))

 
maior_numero = max(numero_1, numero_2, numero_3)
menor_numero = min(numero_1, numero_2, numero_3)

print()
print(f"Numeros informados: {numero_1} | {numero_2} | {numero_3}")

if numero_1 == numero_2 == numero_3:
    print(f"Os números são iguais")
else:
    print()
    print(f"menor numero: {menor_numero}")
    print(f"Maior número {maior_numero}")