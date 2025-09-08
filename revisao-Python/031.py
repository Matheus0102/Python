'''
Escreva um programa que leia diversos alunos, crie um dicionário com as notas de dele em três disciplinas: matemática,
português e história. Em seguida, exiba a média das notas dos alunos.
'''



print('Bem vindo ao Programa de cadastro de alunos, para saber a media entre eles...')

alunos ={}

while True:
    nome = input('Nome[Fim para sair]: ')
    if nome == 'sair':
        break

    matematica = float(input('Matématica: '))
    portugues = float(input('Português: '))
    historia = float(input('História: '))

    alunos[nome] = {'Matématica': matematica, 'Português': portugues, 'Historia': historia}

    for nome, notas in alunos.items():
        media = sum(notas.values()) / len(notas)
        print(f'A média do Aluno {nome} é {round(media, 2)}')