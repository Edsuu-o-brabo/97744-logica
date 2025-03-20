import os
 
os.system("clear")

media = 0
soma = 0

for i in range(4):
    numero = int(input(f"Digite a {i+1}° nota: "))
    soma += numero

media = soma / 4


print()
print(f"Media: {media}")
print("Vai ser pau e pica na xereca da bandida")