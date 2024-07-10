# Data: 09/07/2024
# Exercício: 017 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição:  Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80 Km/h, exiba uma mensagem
#             dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por cada Km acima
#             da velocidade permitida.

# Solicita ao usuário que insira a velocidade do carro
velocidade = float(input("\nQual a velocidade do carro em km/h? "))

# Verifica se a velocidade é menor ou igual a 80 km/h
if velocidade <= 80:
    print("\nVocê está dirigindo dentro do limite de velocidade permitido!")
    print("\nDirija com cuidado!\n\n")
else:  # Calcula a multa: R$ 5,00 por cada Km acima de 80 km/h
    multa = (velocidade - 80) * 5
    print("\n-----------------------<<< ATENÇÃO >>>-----------------------")  # Alerta de excesso de velocidade
    print(f"Você ultrapassou a velocidade máxima permitida de 80 km/h!")
    print(f"Você foi multado em R$ {multa:.2f}")  # Exibe o valor da multa com duas casas decimais
    print(f"Reduza sua velocidade para não receber mais multas!\n\n")
