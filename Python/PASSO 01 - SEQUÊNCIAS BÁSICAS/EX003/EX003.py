# Data: 27/06/2024
# Exercício: 003 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Crie um programa que leia o nome, ano de nascimento e o salário de um funcionário, mostrando no final uma
#            mensagem

# Solicita ao usuário que insira o nome do funcionário
nome = input("Nome do funcionário: ")

# Solicita ao usuário que insira o ano de nascimento do funcionário
ano_nascimento = int(input("Ano de nascimento do funcionário: "))

# Solicita ao usuário que insira o salário do funcionário
salario = float(input("Valor do salário do funcionário: R$ "))

# Exibe a ficha funcional do funcionário
print("\n----------- FICHA FUNCIONAL -----------")
print("Nome:", nome)
print("Ano de nascimento:", ano_nascimento)
print("Salário: R$", salario)  # Imprime o salário do funcionário formatado com duas casas decimais
