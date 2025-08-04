'''
Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000. No final
mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)
'''

# Inicialização das variáveis
contador = 0
soma = 0

print('Bem vindo ao programa!!\n'
      'Digite a quantidade de valores que deseja e no final mostraremos quantos números foram digitados e a soma entre eles.\n'
      '-----------------------\n'
      'Para encerrar o programa e visualizar os resultados, digite 0000')

while True:
    numero = int(input('Digite um Valor: '))

    # Verifica se o número é o flag para sair
    if numero == 0000:
        print(f'Foram {contador} valores digitados.\n'
              f'A soma entre eles foi {soma}')
        break

    # Incrementa o contador e acumula a soma
    contador += 1
    soma += numero