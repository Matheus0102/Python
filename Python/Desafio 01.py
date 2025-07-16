'''
Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário
Saída esperada:
A posição do objeto no tempo x é de y (m)
'''

posicaoInicial = float(input('Informe o valor inicial: '))
velocidadeInicial = float(input('Informe a velocidade Inicial: '))
tempo = float(input('informe o Tempo: '))
aceleracao = float(input('Infore a aceleração: '))

posicaoFinal = posicaoInicial + velocidadeInicial * tempo + (aceleracao * (tempo ** 2))/ 2
print(f'A posição do objeto no tempo {tempo} é de {posicaoFinal} (m)')