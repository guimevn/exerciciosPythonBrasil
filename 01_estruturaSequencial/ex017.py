import math
"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga 
e sempre arredonde os valores para cima, isto é, considere latas cheias."""

a = int(input('Digite a área do quadrado: (m²) '))
lT = (a / 6) * 1.1
latas = lT / 18  # latas de tintas a serem compradas
gal = lT / 3.6  # galões de tintas a serem comprados
print('Você terá que comprar {} latas e terá que pagar R${}'.format(math.ceil(latas), math.ceil(latas) * 80))
print('Você terá que comprar {} galões e terá que pagar R${}'.format(math.ceil(gal), math.ceil(gal) * 25))

mistLatas = int(lT / 18)
mistGal = int((lT - (mistLatas * 18)) / 3.6)
if lT - (mistLatas * 18) % 3.6 != 0:
    mistGal += 1

print('Você terá que comprar {} latas, {} galões e terá que pagar R${:.2f}'.format(mistLatas, mistGal, (mistLatas * 80)
                                                                                   + (mistGal * 25))) 
