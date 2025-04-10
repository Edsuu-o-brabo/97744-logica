import os

os.system("clear")

def calcular_imc(peso, altura):
    """Calcula o IMC dado o peso (kg) e a altura (m)."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Retorna a classificação do IMC com base na tabela da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II (severa)"
    else:
        return "Obesidade grau III (mórbida)"

# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))