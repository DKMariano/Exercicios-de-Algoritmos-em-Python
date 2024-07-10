# Data: 09/07/2024
# Exercício: 018 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela
#            pode ou não votar.


from datetime import datetime  # Importa o módulo datetime para trabalhar com datas

ano_atual = datetime.now().year  # Obtém o ano atual

# Solicita ao usuário que insira o ano de nascimento
ano_nascimento = int(input("\nDigite o ano do seu nascimento: "))

idade = ano_atual - ano_nascimento

print("\n-----------------------<<< TRT informa >>>-----------------------")
print(f"Você tem {idade} anos!")  # Exibe a idade calculada

# Verifica se a idade é suficiente para votar ou não
if idade >= 16:
    print("Você já pode votar!\n\n")
else:
    print("Você NÃO pode votar!\n\n")
