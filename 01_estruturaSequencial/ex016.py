import math
"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e a tinta ser vendida em latas de 18 litros
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

a = int(input('Digite a área do quadrado: (m²) '))
lT = a / 3
latas = lT / 18
print('Você terá que comprar {} tintas e terá que pagar R${}'.format(math.ceil(latas), math.ceil(latas) * 80))


# outro jeito de fazer ->
# if lT % 18 != 0:
#   qtdL += 1