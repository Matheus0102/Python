'''
Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.
'''

idade = int(input('idade: '))
if idade > 16 and idade < 69:

    peso = float(input('Peso: '))
    if peso > 50:

        horas_de_sono = int(input('Horas de sono: '))
        if horas_de_sono > 5:

            bebidas = input('Bebeu nas ultimas 12 horas? [S/N]: ').strip().upper()[0]
            if bebidas == 'N':
                print('Pode doar')
            else:
                print('Não poderia ter bebido nas Ultimas 12h')
        else:
            print('Horas de sono incorreta')
    else:
        print('Peso incorreto')
else:
    print('Idade Incorreta')