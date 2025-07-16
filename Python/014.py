'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''

letra = input('Digite a letra e veja se ela é vogal ou cossoante: ').strip().upper()[0]

#metodo 1
if letra in 'AEIOU':
    print('Vogal')
else:
    print('Consoante')

#metódo 2
if letra == 'A':
    print('Ela é vogal')
elif letra == 'E':
    print('Ela é vogal')
elif letra == 'I':
    print('Ela é vogal')
elif letra == 'O':
    print('Ela é vogal')
elif letra == 'U':
    print('Ela é vogal')
else:
    print('Ela é consoante')
