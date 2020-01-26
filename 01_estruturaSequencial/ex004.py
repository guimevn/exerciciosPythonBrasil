""""Faça um Programa que peça as 4 notas bimestrais e mostre a média"""

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))
med = (n1 + n2 + n3 + n4)/4
print('Com as notas {}, {}, {} e {} a sua média ficará: {:.2f}'.format(n1, n2, n3, n4, med))
 
