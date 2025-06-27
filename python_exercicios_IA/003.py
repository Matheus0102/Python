'''
Desafio 1 — Com while:
Crie um programa que peça números ao usuário até que ele digite 0.
Quando digitar 0, o programa encerra e mostra a soma de todos os números digitados.
'''


soma = 0

numero = int(input('Digite um número (0 para sair): '))

while numero != 0:
    soma += numero  # soma = soma + numero
    numero = int(input('Digite outro número (0 para sair): '))

print('A soma dos números digitados é:', soma)


