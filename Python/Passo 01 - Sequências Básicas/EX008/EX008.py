# Data: 29/06/2024
# Exercício: 008 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.

# Solicita ao usuário que insira a distância em metros
distancia = float(input("\nDigite a distância em metros que você deseja converter: "))

# Exibe o cabeçalho do conversor de distância
print("\n\n-----------<<< Conversor de Distância >>>------------ ")

# Converte e exibe a distância em milímetros, centímetros, decímetros, metros, decâmetros, hectômetros, quilômetros
print(f"Milímetro: {distancia * 1000:.2f} mm.", )
print(f"Centímetro: {distancia * 100:.2f} cm.", )
print(f"Decímetro: {distancia * 10:.2f} dm.")
print(f"Metro: {distancia:.2f} m.")
print(f"Decâmetro: {distancia / 10:.2f} dam.")
print(f"Hectômetro: {distancia / 100:.2f} hm.")
print(f"Quilômetro: {distancia / 1000:.2f} km.\n")
