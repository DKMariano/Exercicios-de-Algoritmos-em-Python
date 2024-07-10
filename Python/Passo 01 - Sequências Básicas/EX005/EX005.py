# Data: 27/06/2024
# Exercício: 005 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na
#            disciplina


# Solicita ao usuário que insira o nome do aluno
nome = input("\nDigite o nome do aluno: ")

# Solicita ao usuário que insira a nota da 1ª avaliação e a converte para float
nota1 = float(input("Digite a nota da 1ª Avaliação: "))
nota2 = float(input("Digite a nota da 2ª Avaliação: "))

# Calcula a média das duas notas
media = (nota1 + nota2) / 2

# Exibe a análise do desempenho do aluno
print("\n\nAnálise do desempenho estudantil do aluno", nome)
print("---------------------------------------------------------------------")
print(f"O aluno tirou nota {nota1} na 1ª Avaliação e nota {nota2} na 2ª Avaliação.")
print(f"Portanto, a MÉDIA de {nome} é {media:.2f}.\n")
