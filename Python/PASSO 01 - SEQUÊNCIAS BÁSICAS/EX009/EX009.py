# Data: 29/06/2024
# Exercício: 009 - Exercícios de Algoritmos (em Python)
# Instituição de Ensino: Estudonauta
# Disciplina: Python
# Professor: Gustavo Guanabara
# Aluno: D. K. Mariano
# Descrição: Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela
#            pode comprar.

real = float(input("\nDigite o valor em reais que deseja converter: R$ "))

print("\n\n-----------<<< Conversor de Moedas >>>------------")
print(f"Valor em REAL: R$ {real:.2f}")
print(f"Valor em DÓLAR: US$ {real / 5.5:.2f}")  # Considerando 1 dólar = R$5,50
print(f"Valor em EURO: € {real / 5.98:.2f}")  # Considerando 1 euro = R$5,98
print(f"Valor em IENE: ¥ {real / 0.035:.2f}")  # Considerando 1 iene = R$0,035
print(f"Valor em LIBRA ESTERLINA: £ {real / 7.06:.2f}")  # Considerando 1 libra esterlina = R$7,06
print(f"Valor em FRANCO SUÍÇO: RCHF {real / 6.22:.2f}")  # Considerando 1 franco suíço = R$6,22
print("\n\n")
