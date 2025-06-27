'''
Escreva um programa que converta real para o Franco Congolês
Saída esperada:
10,00 reais, equivalem a 5052,00 Francos Congoleses

'''

real = int(input('Digite o valor em real: '))
francoCongolês = real / float(0.0019)

print(f'{real} reais, equivalem a {francoCongolês} Francos Congoleses')