import os

os.system("clear")

valor = float(input("Digite o valor do produto: "))

print(""" 
-----------------FORMA DE PAGAMENTO-----------------
    1    \tÀ vista 
    2    \tÀ prazo
""")

forma_de_pagamento = int(input("Digite a Forma de Pagmento:  "))
 
match forma_de_pagamento:
  case 1: 
    desconto = valor * 0.10
    total = valor - desconto
    print()
    print(f"Valor: {valor}")
    print(f"forma de pagamento: ")    







