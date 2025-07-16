'''
Crie um programa que leia uma frase e mostre:
1- Quantas vezes aparece a letra “a”
2- Em que posição ela aparece a primeira vez
3- Em que posição ela aparece na última vez
'''

frase = input('Digite sua frase: ').strip().lower()

frase = frase.replace('á','a')
frase = frase.replace('à','a')
frase = frase.replace('â','a')
frase = frase.replace('ã','a')

print(f'A letra a aparece {frase.count('a')} vezes\n'
      f'Ela aparece pela primeira vez na posição: {frase.find('a') +1}\n'
      f'Posição do Último a: {frase.rfind('a') + 1}')