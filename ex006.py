import math
""""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""

r = int(input('Digite o raio do círculo: '))
a = math.pi * r ** 2
print('A área do círculo com o raio {} é igual a: {:.2f}'.format(r, a))
