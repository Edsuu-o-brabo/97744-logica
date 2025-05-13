import os
from dataclasses import dataclass
os.system('cls || clear')


@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str


lista_clientes = [] # Criando uma lista para adicionar clientes.
QUANTIDADES_CLIENTES = 2 # Constantes que define a quantidade de clientes.

# Laço de repetição para adicionar clientes.
print("Informe os dados do cliente:")
for i in range(QUANTIDADES_CLIENTES):
    cliente = Cliente( # Instanciando um objeto
        nome = input("Nome: "), # Não esqueça da virgula.
        email = input("E-mail: "),
        telefone= input("Telefone: ") # No último não tem virgula.
    )
    lista_clientes.append(Cliente) # Adicionando um cliente na lista. 
    print()

# Laço de repetiçãopara exibir dados dos clientes.
print('\n= Exibindo dados Clientes =')
for cliente in lista_clientes: # Mostra os dados por elementos na lista.
    print(f"Nome:{cliente.nome} ")
    print(f"E-mail:{cliente.email} ")
    print(f"Telefone:{cliente.telefone} ")
    print()