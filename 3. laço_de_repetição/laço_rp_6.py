import os 

os.system("Clear")
 
n1 = int(input("Digite o Numero desejado:  "))

print("Tabuado do numero desejado: ")

for i in range(1 , 101):
   resultado = n1 * i 
   print(f"{n1} x {i} = {resultado}")