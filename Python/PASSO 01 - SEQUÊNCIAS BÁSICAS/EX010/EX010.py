# Data: 29/06/2024
# Exercício: 010 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a
#            quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros
#            quadrados.

largura = float(input("\nDigite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura

tinta = area / 2

print("\n\n-----------<<< Calculadora de Tinta >>>------------")
print(f"Área a ser pintada: {area} m²")
print(f"Quantidade de tinta necessária:  {tinta} l\n\n")
