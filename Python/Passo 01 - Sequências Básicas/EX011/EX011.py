# Data: 29/06/2024
# Exercício: 011 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de
#            Delta.


# Solicita ao usuário que insira os coeficientes da equação do segundo grau
print("\nEquação: ax² + bx + c")
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# Calcula o valor de Delta usando a fórmula Delta = b² - 4ac
delta = (b*b) - (4 * a * c)

# Exibe a equação informada pelo usuário
print(f"\nEquação: {a}x² + {b}x + {c}")

# Exibe o valor de Delta calculado
print(f"\nDelta: {delta}")
