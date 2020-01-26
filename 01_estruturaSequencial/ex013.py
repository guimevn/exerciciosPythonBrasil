""""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

HouM = str(input('Você é homem ou mulher?: [H/M] ')).lower()
alt = float(input('Qual é a sua altura?: '))
if HouM == 'h':
    print('O seu peso ideal é: {:.2f}'.format((72.7*alt) - 58))
else:
    print('O seu peso ideal é: {:.2f}'.format((62.1*alt) - 44.7))
