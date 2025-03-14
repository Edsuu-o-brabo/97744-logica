import os 
import time
os.system("Clear")

n1 = int(input("Digie um numero:  "))

print("Contagem Regressiva")
for i in range(n1,0, -1):
    print(f"Contagem : {i}")
    time.sleep(5000000000)
