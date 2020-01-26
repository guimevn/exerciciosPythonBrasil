""""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

int1 = int(input('Digite um número inteiro: '))
int2 = int(input('DIgite outro número inteiro: '))
fl1 = float(input('Digite um número real: '))
print('O produto do dobro do primeiro com metade do segundo: {}'.format((int1 * 2) * (int2*0.5)))
print('A soma do triplo do primeiro com o terceiro: {}'.format((int1 * 3) + fl1))
print('O terceiro elevado ao cubo: {:.3f}'.format(fl1 ** 3))
 
