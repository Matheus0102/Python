'''
Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.
'''

idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso(Kg): '))
consumoDeBebidaAlcolica = input('Digite S se teve consumo de bebida alcólica nas ultimas 12 horas, ou N: ').strip()
tatuagem = input('Digite S se possui alguma tatuagem ou se caso não tiver nenhuma tatuagem digite N: ').strip()
horasDeSono = input('Dormiu mais de 6 horas na noite passada? S ou N: ').strip()

if idade >= 18 and idade < 69 and peso > 50 and consumoDeBebidaAlcolica == 'n' and tatuagem == 'n' and horasDeSono == 's' :
    print('Esta apto a ser doador de sangue!')
elif idade == 16 or idade < 18 :
    print('Esta apto, porem, com acompanhamento de responsáveis para menores de 18!')
elif consumoDeBebidaAlcolica == 'sim':
    print('Não está apto para ser doador de sangue devido ao consumo de bebida alcólia nas ultimas 12 horas')
elif tatuagem == 'sim':
    print('Não está apto para ser doador de sangue devido a possuir tatuagem')
elif horasDeSono == 'nao':
    print('Não está apto para ser doador de sangue devido não ter tido o minímo de horas de sono na noite passada!')
else:
    print('Não está apto para ser doador de sangue!')
