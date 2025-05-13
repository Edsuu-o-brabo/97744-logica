class Funcionario:
    def __init__(self, nome, data_admissao, matricula, endereco):
        self.nome = nome
        self.data_admissao = data_admissao
        self.matricula = matricula
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome},{self.data_admissao},{self.matricula},{self.endereco}"


class Cliente:
    def __init__(self, nome, data_nascimento, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome},{self.data_nascimento},{self.endereco}"


def salvar_dados(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for item in lista:
            arquivo.write(str(item) + "\n")


def ler_dados(nome_arquivo, tipo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            print(f"\nDados de {tipo}s:")
            for i, linha in enumerate(linhas, 1):
                print(f"{i}º {tipo}: {linha.strip()}")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")


# Programa principal
funcionarios = []
clientes = []

print("Cadastro de Funcionários:")
for i in range(3):
    nome = input("Nome: ")
    data_admissao = input("Data de admissão: ")
    matricula = input("Matrícula: ")
    endereco = input("Endereço: ")
    funcionario = Funcionario(nome, data_admissao, matricula, endereco)
    funcionarios.append(funcionario)

print("\nCadastro de Clientes:")
for i in range(3):
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Endereço: ")
    cliente = Cliente(nome, data_nascimento, endereco)
    clientes.append(cliente)

# Salvando dados em arquivos
salvar_dados(funcionarios, "funcionarios.txt")
salvar_dados(clientes, "clientes.txt")

# Lendo e mostrando os dados
ler_dados("funcionarios.txt", "Funcionário")
ler_dados("clientes.txt", "Cliente")