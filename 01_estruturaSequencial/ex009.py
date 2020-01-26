""""Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius."""

f = int(input('Digite a temperatura em graus Farenheit: '))
c = (f - 32) * 5/9
print('A temperatura em graus Celsius é: {:.2f}'.format(c))
 
