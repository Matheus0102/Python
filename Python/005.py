'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
V = (4/3) . π . r³
A = 4 . π . r²
Saída esperada:
Volume da Esfera: Y
Área da esfera: X
'''

raio = int(input('Digite o Raio da esfera: '))

volumeEsfera = (4/3) * 3.14 * raio ** 3
areaEsfera = 4 * 3.14 * raio ** 2

print(f'Volume da esfera: {volumeEsfera} '
      f'Area da esfera: {areaEsfera} ')