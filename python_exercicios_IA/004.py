'''
Fazer uma versão que também mostre a quantidade de números digitados.
e que calcule a média dos números.
'''

soma = 0
contador = 0

numero = int(input('Digite um número (0 para sair): '))

while numero != 0:
    soma += numero  # somando os números
    contador += 1   # contando quantos números foram digitados
    numero = int(input('Digite outro número (0 para sair): '))

if contador > 0:
    media = soma / contador
    print('A soma dos números é:', soma)
    print('Quantidade de números digitados:', contador)
    print('A média dos números é:', media)
else:
    print('Nenhum número foi digitado.')