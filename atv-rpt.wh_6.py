import os
import time

os.system("cls || clear")

soma_notas = 0
contador = 0
media = 0

while True:
    nota = float(input("Digite uma nota: "))  
    soma_notas += nota  
    contador += 1  

    continuar = input("Deseja digitar mais uma nota? (Sim/Não): ")
    if continuar == 'Não':
        break  
   

media = soma_notas / contador

print(f"\nQuantidade de notas inseridas: {contador}")
print(f"Média das notas: {media:.2f}")
if media >= 7:
     print("APROVADO!")
elif 5 <= media < 7:
            print("RECUPERAÇÃO!")
else:
            print("REPROVADO!")
    