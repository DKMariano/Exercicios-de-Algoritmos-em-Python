# Data: 27/06/2024
# Exercício: 006 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.

# Solicita ao usuário que insira um número inteiro
numero = int(input("\nDigite um número inteiro: "))

# Calcula o antecessor e sucessor do número inserido
antecessor = numero - 1
sucessor = numero + 1

# Exibe o número inserido e seu antecessor e sucessor
print(f"\n-------<<< Análise o número {numero} >>>-------")
print(f"Antecessor:{antecessor}")
print(f"Sucessor:{sucessor}")
