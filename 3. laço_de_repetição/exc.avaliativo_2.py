import os

os.system("clear")

salarios = []
idades = []
mulheres_5k = 0

while True:
    print("\nMENU:")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        os.system("cls" if os.name == "nt" else "clear")  
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").strip().upper()
        salario = float(input("Salário: "))

        idades.append(idade)
        salarios.append(salario)

        if sexo == "F" and salario >= 5000:
            mulheres_5k += 1

    elif opcao == "2":
        if not salario:
            print("Nenhum dado cadastrado.")
        else:
            print(f"Média salarial: R$ {sum(salarios) / len(salarios):.2f}")
            print(f"Maior idade: {max(idades)} | Menor idade: {min(idades)}")
            print(f"Mulheres com salário ≥ R$ 5000,00: {mulheres_5k}")

    elif opcao == "3":
        print("Encerrando...")
        break
    else:
        print("Opção inválida! Tente novamente.")










