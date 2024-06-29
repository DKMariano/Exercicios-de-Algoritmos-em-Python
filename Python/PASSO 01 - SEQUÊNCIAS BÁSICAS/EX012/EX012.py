# Data: 29/06/2024
# Exercício: 012 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição:  Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de
#             desconto.

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))

desconto = 5.0 / 100.0

novo_preco = preco * (1 - desconto)

print("\n-----------<<< LOJAS TITA >>>------------")
print(f"Produto: {produto}")
print(f"Preço: R$ {preco:.2f}")
print(f"Desconto: - R$ {preco * desconto:.2f}")
print(f"Valor a pagar: R$ {novo_preco:.2f}")
