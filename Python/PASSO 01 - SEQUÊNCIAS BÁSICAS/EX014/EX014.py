# Data: 01/07/2024
# Exercício: 013 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição:  A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a
#             quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#             Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

km_percorridos = float(input("\nDigite a quantidade de quilômetro  percorridos pelo carro: "))
dias = int(input("Digite a quantidade de dias que o carro ficou alugado: "))
aluguel = (dias * 90) + (km_percorridos * 0.20)

print("\n============== CALCULADORA DE ALUGUEL ==============")
print(f"Km percorridos: {km_percorridos} km ")
print(f"Quantidade de  dias  de aluguel: {dias}")
print(f"Valor a pagar: R$ {aluguel:.2f}")
