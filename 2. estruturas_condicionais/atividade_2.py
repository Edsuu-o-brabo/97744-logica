import os

os.system("clear") # Limpa o Terminal
 
n1 = float(input("Digite sua primeira nota: "))     
n2 = float(input("Digite sua terceira nota: ")) 
n3 = float(input("Digite sua segunda nota nota: ")) 
#processamento

media = (n1 + n2 + n3) / 3

print()
print(f"Média: {media} ")

if media < 7:
  print("Reprovado" )

else: 
   print("Aprovado!")  