import os 

os.system("clear")

def media():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    
    return (n1 + n2 + n3) / 3

resultado = media()

if media >= 7 :
   resultado2 = "Aprovado"
else: media >= 7
resultado2 = "Reprovado"



print(f"Média: {resultado:.2f}")
print(f"Resultado: {resultado2}")