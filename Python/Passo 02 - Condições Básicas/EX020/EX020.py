# Data: 09/07/2024
# Exercício: 020 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição:  Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

# Solicita ao usuário que insira um número inteiro maior que zero
numero = int(input("\nDigite um número inteiro maior que zero: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"\nO número {numero} é par! \n\n")

else:
    print(f"\nO número {numero} é ímpar!\n\n")
