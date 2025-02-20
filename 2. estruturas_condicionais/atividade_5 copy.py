import os

os.system("clear")
#OPÇÃO 1


idade = int(input("Digite sua idade:  "))

if idade < 18 or idade > 65:
   print("Você não é obrigado a votar! :)")
else :
   print("É obrigado a votar :)  ")

 #OPÇÃO 2.
if idade >= 18 and idade <= 65:
   print("É obrigado a votar!")
else:
   print("Não é obrigado a votar!")