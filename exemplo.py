import os
 
os.system("clear")


while True: 
    n1 = int(input("Digite  a sua nota:   "))    

    if n1 < 1 or n1 > 10: 
        print("Não autorizado. \nNota não encontarda")
    else: 
        break
print()
print(f"Nota informada: {n1}")
print("ACABOU CARALHO")

