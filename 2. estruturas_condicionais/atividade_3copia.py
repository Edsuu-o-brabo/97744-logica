import os

os.system("clear") # Limpa o Terminal

numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))

#Processamento
soma = numero_1 + numero_2
media = (numero_1 + numero_2) / 2
produto = numero_1 * numero_2 
 
maior_numero = max(numero_1, numero_2)
menor_numero = min(numero_1, numero_2)

print()
print(f"Soma: {soma} ")
print(f"Produto: {produto} ")
print(f"Média: {media}")
print(f"Maior número {maior_numero}")
print(f"menor numero: {menor_numero}")