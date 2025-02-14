import os

os.system("clear") # Limpa o Terminal

numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))

#Processamento
soma = numero_1 + numero_2
media = (numero_1 + numero_2) / 2
produto = numero_1 * numero_2 

if numero_1 < numero_2:
    maior_numero = numero_2
    menor_numero = numero_1

else: 
    maior_numero = numero_2
    menor_numero = numero_1

print()
print(f"Soma: {soma} ")
print(f"Produto: {produto} ")
print(f"Média: {media}")

if numero_1 == numero_2:
    print(f"Os números são iguais")
else: 
     print(f"Maior número {maior_numero}")
     print(f"menor numero: {menor_numero}")