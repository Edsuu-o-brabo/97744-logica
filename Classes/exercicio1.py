import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float


print()

pessoa2 = Pessoa(nome = input("Digite o nome: "),
    idade = int(input("Digite a idade: ")),
    peso = float(input("Digite o peso: ")),
    altura = float(input("Digite a altura: "))
    )

    
print("\n= Dados da Pessoa =")
print(f"\nNome: {pessoa2.nome}, idade: {pessoa2.idade} anos. ")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade} anos. ")