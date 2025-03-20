import os 
os.system("clear")

soma = int 
media = float

while True: 
    for i in range(2):
     n1 = int(input(f"Digite a {i+1}° nota: "))

    media = (n1 + i) / 2
    
    if n1 < 1 or n1 > 10: 
        print({media})
    else: 
        break
print()
print(f"Nota informada: {n1}")
print(f"A sua media foi : {media}")