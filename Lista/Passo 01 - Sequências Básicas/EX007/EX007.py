# Data: 29/06/2024
# Exercício: 007 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.

# Solicita ao usuário que insira um número real
numero = float(input("\nDigite um número real qualquer: "))

# Calcula o dobro, terça parte, quadrado e raiz quadrada  do número inserido
dobro = numero * 2
terca_parte = numero / 3
quadrado = numero * numero
raiz = numero ** (1/2)

# Exibe o número inserido e seus resultados
print(f"\n-------<<< Análise do número {numero} >>>-------")
print(f"Dobro: {dobro:.2f}")
print(f"Terça parte: {terca_parte:.2f}")
print(f"Elevado ao quadrado: {quadrado:.2f} ")
print(f"Raiz quadrada: {raiz:.2f}")
