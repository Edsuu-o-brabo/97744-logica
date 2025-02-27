import os

os.system("clear")

opcao = int(input("Digite o numero: "))

match opcao:
 case 1:
  semana = "Domingo"
  competencia ="Não Util"
 case 2:
  semana = "Segunda-Feira"
  competencia = "Dia da semana util"
 case 3:
  semana = "Terça-Feira"
  competencia = "Dia da semana util"
 case 4:
  semana = "Quarta-feira"
  competencia = "Dia da semana util"
 case 5:
  semana = "Quinta-feira"
  competencia = "Dia da semana util"
 case 6: 
  semana = "Sexta-Feira" 
  competencia = "Dia da semana util"
 case 7: 
  semana = "Sabadoo"
  competencia = "Não Util"
 case _: 
  semana = "Não existente "
  competencia = "Não identificado"
 
import os

os.system("clear")


print(f"Dia da semana: {semana}")
print("")
print(f"Competencia: {competencia}")