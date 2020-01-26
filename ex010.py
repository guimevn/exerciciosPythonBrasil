"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

c = int(input('Digite a temperatura em graus Celsius: '))
f = (c * 9/5) + 32
print('A temperatura em graus Fahrenheit: {:.2f}'.format(f))
