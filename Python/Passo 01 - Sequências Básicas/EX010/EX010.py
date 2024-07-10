# Data: 29/06/2024
# Exercício: 010 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição:  Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a
#             quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros
#             quadrados.

# Solicita ao usuário que insira a largura e altura da parede em metros
largura = float(input("\nDigite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcula a área da parede multiplicando largura por altura
area = largura * altura

# Calcula a quantidade de tinta necessária dividindo a área por 2 (cada litro de tinta pinta 2 metros quadrados)
tinta = area / 2

# Exibe o cabeçalho da calculadora de tinta
print("\n\n-----------<<< Calculadora de Tinta >>>------------")

# Exibe a área a ser pintada formatada com duas casas decimais
print(f"Área a ser pintada: {area:.2f} m²")

# Exibe a quantidade de tinta necessária formatada com duas casas decimais
print(f"Quantidade de tinta necessária: {tinta:.2f} litros\n\n")
