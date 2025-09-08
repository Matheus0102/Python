'''
Escreva um programa que crie uma lista com varios números lidos pelo usuário, em seguida, exiba apenas os números ímpares da lista.
'''

print('Seja bem vindo')
numeros = []

while True:

    try:
        n = input('Digite um numero[0000 para sair]: ')
        if n == '0000':
            break

        numeros.append(int(n))
    except :
        numeros.append(int(input('Digite incorreto, digite apenas valores numericos: ')))
        resposta = input('Digito incorreto, digite apenas sim ou não para continuar? [S/N]: ').strip().upper()[0]

numeros_impare = [x for x in numeros
                  if x % 2 != 0]

print(f'Os numeros ímpares são: {numeros_impare}')









