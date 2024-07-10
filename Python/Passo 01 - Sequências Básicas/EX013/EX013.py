# Data: 01/07/2024
# Exercício: 013 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição:  Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de
#             aumento.

# Solicita ao usuário que insira o nome e o salário do funcionário
nome = input("\nDigite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário em reais: R$ "))

# Define a taxa de aumento de 15% (ou 0.15)
aumento = 0.15

# Calcula o novo salário com o aumento aplicado
novo_salario = salario * (1 + aumento)

# Exibe o cabeçalho da calculadora de salário e os detalhes do cálculo
print("\n-------<<< CALCULADORA DE SALÁRIO >>>-------")
print(f"Nome do funcionário: {nome}")
print(f"Salário Anterior: R$ {salario:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
print(f"Aumento: R$ {salario * aumento:.2f}")
