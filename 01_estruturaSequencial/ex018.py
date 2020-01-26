"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

mb = float(input('Qual o tamanho do arquivo para download? (mB) '))
mbps = float(input('Qual a velocidade de download? (mbps) '))
velD = mb / (mbps / 8)
print('Você levará {:.2f}min para baixar o arquivo.'.format(velD / 60))
 
