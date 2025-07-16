'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1- O nome com todas as letras maiúsculas
2- O nome com todas minúsculas
3- Quantas letras ao todo (sem considerar os espaços)
4- Quantas letras tem o primeiro nome
'''

nome = input('Digite o seu nome: ').strip()

#1- O nome com todas as letras maiúsculas
print(nome.upper())

# 2- O nome com todas minúsculas
print(nome.lower())

quantidadeEspacos = nome.count(' ')
contarCaracteres = len(nome)

letraSemEspacos = contarCaracteres - quantidadeEspacos

print(letraSemEspacos)

primeiroNome = nome.find(' ') -1
print(primeiroNome)
