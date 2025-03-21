import os

os.system("Clear")

print("""
=========== MENU ============
código  /tprato     /tvalor
1  \t\tpicanha   \t\t25,00
2    \t\tlasanha    \t\t20,00
3     \t\tstrogonoff  \t\t18,00
4    \t\tbife acebolado \t\t15,00
5      \t\tpão com ovo \t\t5,00    
        """)

import os
os.system("cls | clear")

def main():
    pratos = [
        ("Prato 1", 20.00),
        ("Prato 2", 35.00),
        ("Prato 3", 15.00),
        ("Prato 4", 25.00),
        ("Prato 5", 40.00)
    ]

    total = 0
    pedidos = []

    while True:
        print("\n---- MENU ----")
        for i, (nome, preco) in enumerate(pratos, 1):
            print(f"{i}. {nome} - R$ {preco:.2f}")

        escolha = int(input("Escolha o número do prato (1-5): ")) - 1
        if 0 <= escolha < len(pratos):
            nome, preco = pratos[escolha]
            pedidos.append((nome, preco))
            total += preco

        if input("Deseja escolher outro prato? (s/n): ").strip().lower() != 's':
            break

    print("\n----- Seus pedidos -----")
    for nome, preco in pedidos:
        print(f"{nome}: R$ {preco:.2f}")

    print(f"\nTotal: R$ {total:.2f}")
    if input("Deseja pagar 10% de gorjeta? (s/n): ").strip().lower() == 's':
        gorjeta = total * 0.10
        total += gorjeta
        print(f"Gorjeta (10%): R$ {gorjeta:.2f}")
    
    print(f"Total final: R$ {total:.2f}")

if __name__ == "__main__":
    main()

    


