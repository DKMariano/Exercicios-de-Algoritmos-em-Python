# Data: 01/07/2024
# Exercício: 013 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Escreva um programa para calcular a redução do tempo de vida de um fumante.
#            Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou.
#            Considere que um fumante perde 10 min de vida a cada cigarro.
#            Calcule quantos dias de vida um fumante perderá e exiba o total em dias.


# Solicita ao usuário que insira a quantidade de cigarros fumados por dia e há quantos anos ele fuma
cigarros = float(input("\nQuantos cigarros você fuma por dia? "))
anos_fumando = float(input("Você fuma há quantos anos? "))

# Calcula o total de minutos perdidos
# - 10 minutos perdidos por cigarro * número de cigarros por dia * número de dias fumados em um ano
minutos_perdidos = 10 * cigarros * anos_fumando * 364

# Converte os minutos perdidos em dias e anos perdidos
dias_perdidos = minutos_perdidos // 1440
anos_perdidos = dias_perdidos // 365

# Exibe o cabeçalho da calculadora de vida e os resultados
print("\n-----------------------<<< CALCULADORA DE VIDA >>>-----------------------")
print(f"Você já perdeu {minutos_perdidos:.0f} minutos da sua vida por causa do cigarro.")
print(f"Isso equivale a {dias_perdidos:.0f} dias de vida, ou aproximadamente {anos_perdidos:.0f} anos.")
