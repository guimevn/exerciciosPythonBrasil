""""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58 """

alt = float(input('Digite a sua altura: '))
print('O seu peso ideal seria: {:.2f}'.format((72.7 * alt) - 58))
