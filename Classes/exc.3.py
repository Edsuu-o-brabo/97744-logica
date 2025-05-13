import os
from dataclasses import dataclass
os.system('cls || clear')


@dataclass
class Autor:
    nome: str
    biografia: str


@dataclass
class Livro:
    titulo: str
    ano: int
   

autor = Autor( 
        nome = input("Machado de Assis "), 
        biografia = input("Joaquim Maria Machado de Assis foi um escritor brasileiro, amplamente reconhecido por críticos, estudiosos, escritores e leitores como o maior expoente da literatura brasileira.")        
)


livro = Livro( 
        titulo = input("Memórias Póstumas de Brás Cubas"), 
        ano = input("1881")    
)