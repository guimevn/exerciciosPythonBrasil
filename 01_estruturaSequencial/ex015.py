"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao IR.
quanto pagou ao sindicato.
o salário líquido."""

salH = float(input('Quanto você ganha por horas trabalhada? R$'))
hrsM = int(input('Quantas horas você trabalha por mês? '))
salB = salH * hrsM
INSS = salB * 8/100
IR = salB * 11/100
SIN = salB * 5/100
print('O seu salário bruto será de: R${}', salB)
print('O seu salário - INSS (8%): R${}'.format(salB - INSS))
print('O seu salário - IR (11%): R${}'.format(salB - IR))
print('O seu salário - Sindicato (5%): R${}'.format(salB - SIN))
print('O seu salário líquido: R${}'.format(salB - INSS - IR - SIN))
