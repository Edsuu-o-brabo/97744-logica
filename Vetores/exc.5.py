import os
os.system("cls" if os.name == "nt" else "clear")

list_numeros = []
QUANTIDADE = 6

def im_pa(numero, pares, impares):
    if numero % 2 == 0:
        pares += 1
    else: 
        impares += 1
    return pares, impares    

pares = 0
impares = 0

for i in range(QUANTIDADE):
    n1 = int(input("Digite o número: "))
    list_numeros.append(n1)
    pares, impares = im_pa(n1, pares, impares)

print("\nNúmeros digitados:", list_numeros)
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")