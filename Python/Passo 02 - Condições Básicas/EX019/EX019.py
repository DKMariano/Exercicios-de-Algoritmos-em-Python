# Data: 09/07/2024
# Exercício: 019 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição:  Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela.
# #             No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima de 7.0)

# Exibe o cabeçalho do cadastro de aluno
print("\n-------------------------------------<<< CADASTRO DE ALUNO >>>-----------------------------------\n")

# Solicita ao usuário que insira o nome do aluno
nome = input("Nome do aluno: ")

# Solicita ao usuário que insira as notas da 1ª e 2ª avaliações
nota1 = float(input("Nota 1ª Avaliação: "))
nota2 = float(input("Nota 2ª Avaliação: "))

# Calcula a média das notas
media = (nota1+nota2) / 2

# Exibe a análise do desempenho do aluno
print(f"\nAnálise do desempenho estudantil do aluno {nome}")
print("-------------------------------------------------------------------------------------------------")
print(f"O aluno {nome} tirou nota {nota1:.1f} na 1ª Avaliação e nota {nota2:.1f} na 2ª Avaliação. ")
print(f"Logo, a média do aluno {nome} é {media:.1f}.")

# Verifica se o aluno foi aprovado ou reprovado com base na média 7.0
if media >= 7.0:
    print("O aluno foi APROVADO!\n\n")
else:
    print("O aluno foi REPROVADO!\n\n")
