import os
os.system("cls" if os.name == "nt" else "clear")

def mix_min(numeros):
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)

maior, menor = mix_min(numeros)

print()
print(f"O maior número foi: {maior}")
print(f"O menor número foi: {menor}")
