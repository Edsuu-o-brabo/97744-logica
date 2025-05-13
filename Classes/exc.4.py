class Funcionario:
    def __init__(self, nome, data_nascimento, rg, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.rg = rg
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome},{self.data_nascimento},{self.rg},{self.cpf}"


def salvar_funcionarios(lista_funcionarios, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for funcionario in lista_funcionarios:
            arquivo.write(str(funcionario) + "\n")


def ler_funcionarios(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, data_nascimento, rg, cpf = linha.strip().split(',')
                print(f"Nome: {nome}, Data de Nascimento: {data_nascimento}, RG: {rg}, CPF: {cpf}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")


# Programa principal
funcionarios = []

for i in range(5):
    print(f"\nInforme os dados do {i+1}º funcionário:")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    funcionario = Funcionario(nome, data_nascimento, rg, cpf)
    funcionarios.append(funcionario)

salvar_funcionarios(funcionarios, "Funcionarios.txt")
print("\nFuncionários salvos no arquivo. Lendo dados do arquivo...\n")
ler_funcionarios("Funcionarios.txt")
