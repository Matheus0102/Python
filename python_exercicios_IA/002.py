'''
Crie um programa que:
Pergunta ao usuário sua idade
Verifica:
Se tem menor que 12 anos, imprime "Criança"
Se tem entre 12 e 17, imprime "Adolescente"
Se tem entre 18 e 59, imprime "Adulto"
Se tem 60 ou mais, imprime "Idoso"
➕ Desafio bônus:
Verifique se o usuário digitou uma idade válida (não pode ser negativa).
'''

idade = int(input('Digite sua idade: '))

if idade < 0:
    print('Idade inválida')
elif idade < 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')
