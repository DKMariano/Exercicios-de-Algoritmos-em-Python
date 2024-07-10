# Data: 01/07/2024
# Exercício: 013 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário,
#            sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.


# Solicita ao usuário que insira o nome do funcionário e a quantidade de dias trabalhados no mês
nome = input("\nDigite o nome do funcionário: ")
dias_trabalhados = int(input("Digite a quantidade de dias trabalhados durante o mês: "))

# Calcula o salário baseado nos dados fornecidos:
# - 8 horas por dia * R$25 por hora * número de dias trabalhados
salario = dias_trabalhados * 8 * 25

# Exibe o cabeçalho da calculadora de salário e os detalhes do cálculo
print("\n-------<<< CALCULADORA DE SALÁRIO >>>-------")
print(f"Nome do funcionário: {nome}")
print(f"Dias Trabalhados: R$ {dias_trabalhados}")
print(f"Salário: R$ {salario:.2f}")
