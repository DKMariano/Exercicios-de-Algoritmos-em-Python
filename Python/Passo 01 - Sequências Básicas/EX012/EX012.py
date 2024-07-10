# Data: 29/06/2024
# Exercício: 012 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição:  Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de
#             desconto.

# Solicita ao usuário que insira o nome e o preço do produto
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))

# Calcula o desconto de 5% sobre o preço do produto
desconto = 5.0 / 100.0

novo_preco = preco * (1 - desconto)

# Exibe o cabeçalho da loja e os detalhes do produto e do desconto aplicado
print("\n-----------<<< LOJAS TITA >>>------------")
print(f"Produto: {produto}")
print(f"Preço: R$ {preco:.2f}")
print(f"Desconto: - R$ {preco * desconto:.2f}")
print(f"Valor a pagar: R$ {novo_preco:.2f}")
