import os

os.system("clear") 

numero_macas = int(input("Digite a quantidade de maçãs: "))

print()

print(f"Numero de maçãs: {numero_macas}")

if numero_macas < 12:
    numero_macas = numero_macas * 1.30
    
 
else:
    numero_macas = numero_macas * 1.00

print(f"Preço total: {numero_macas:.2f}")
