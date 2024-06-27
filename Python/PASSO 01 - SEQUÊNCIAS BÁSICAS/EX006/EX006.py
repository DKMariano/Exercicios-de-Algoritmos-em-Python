# Data: 27/06/2024
# Exercício: 006 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Faça um programa que leia um número inteiro e mostre o seu antecessor  e seu sucessor.

numero = int(input("\nDigite um número inteiro: "))
antecessor = numero - 1
sucessor = numero + 1

print(f"\n-------<<< Análise o número {numero} >>>-------")
print(f"Antecessor:{antecessor}")
print(f"Sucessor:{sucessor}")
