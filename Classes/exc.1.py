import os
from dataclasses import dataclass

# Limpa o terminal.
os.system("cls || clear")

# Criando uma classe.
@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

#Aplicativo características da classe.
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

#Aplicativo características da classe.
pet1 = Pet("Desgraçadão", 4, 7.8)
pet2 = Pet("Bob Marley", 6,9.2)

print("\n= Dados da Pessoa =")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade} anos.")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade} anos.")

print("\n= Dados da Pessoa =")
print(f"Nome: {pet1.nome}, idade: {pet1.idade} anos, peso: {pet1.peso}")
print(f"Nome: {pet2.nome}, idade: {pet2.idade} anos, peso: {pet2.peso}")
