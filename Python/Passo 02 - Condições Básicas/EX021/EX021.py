# Data: 10/07/2024
# Exercício: 021 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.


# Solicita ao usuário que insira um ano
ano = int(input("\nDigite um ano qualquer: "))

# Verifica se o ano é bissexto
if ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0):
    print(f"\nO ano de {ano} É ano bissexto.\n\n")
else:
    print(f"\nO ano de {ano} NÃO É ano bissexto.\n\n")
