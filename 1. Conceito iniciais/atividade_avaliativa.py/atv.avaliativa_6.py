import os
os.system("clear")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/ 2
print(f"Média: {media:}")

if media >= 6:
    print("Parabéns! Você está aprovado. Você é o futuro do senai")
elif media >= 4:
    print("Você está em recuperação. Você é a tristeza do senai")
else:
    print("Você está reprovado.")
