import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Endereco: 
    logradouro: str
    numero : int 

 

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco : Endereco


    def exebir_dados(self):
        print(f"Nome : {self.nome}")
        print(f"\nIdade : {self.idade}")
        print(f"\nEndereço : {self.endereco.logradouro}, Número: {self.endereco.numero}")

endereco1 = Endereco("Rua A", 23)
pessoa1 = Pessoa("Marta" , 44, endereco1)
pessoa1.exebir_dados()

print()
endereco2 = Endereco("Rua B", 3)
pessoa2 = Pessoa("SAvinho" , 44, endereco2)
pessoa2.exebir_dados()
