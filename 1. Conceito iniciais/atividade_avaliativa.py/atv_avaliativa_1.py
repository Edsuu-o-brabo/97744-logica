import os 

os.system("clear")

numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))
numero_3 = int(input("Digite o terceiro numero: "))

if  numero_1 + numero_2 < numero_3:
 print()
 print("A soma do primeiro numero e do segundo é menor que o terceiro")
else: 
   numero_1 + numero_2 >numero_3
   print()
   print("A soma do primeiro numero e do segundo é maior que o terceiro")

print()
print(f"Soma do 1 e 2:{numero_1 + numero_2}")
print(f"Terceiro numero:{numero_3}")