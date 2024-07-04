# Data: 01/07/2024
# Exercício: 013 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição:  Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de
#             aumento.

nome = input("\nDigite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário em reais: R$ "))
aumento = 0.15
novo_salario = salario * (1 + aumento)
print("\n-------<<< CALCULADORA DE SALÁRIO >>>-------")
print(f"Nome do funcionário: {nome}")
print(f"Salário Anterior: R$ {salario:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
print(f"Aumento: R$ {salario * aumento:.2f}")
