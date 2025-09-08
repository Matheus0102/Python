'''
Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:
Quantas pessoas foram cadastradas
Uma listagem com as pessoas com o maior QI
Uma listagem com as pessoas de menor QI
'''

lista_principal = [[], []]
resposta = ''

print('Digite o nome das pessoas e o QI delas...\n'
      'Digite [0000] para sair!')

while True:

      resposta = input('Digite o nome: ')
      if resposta == '0000':
            break

      lista_principal[0].append(resposta)
      lista_principal[1].append(int(input('Digite o QI: ')))

print(f'Quantidade de pessoas cadastradas: {len(lista_principal[0])}')

maior_QI = sorted(lista_principal[1], reverse=True)
menores_QI = sorted(lista_principal[1])

for i in maior_QI:
      print(lista_principal[0][lista_principal[1].index(1)])

for i in menores_QI:
      print(lista_principal[0][lista_principal[1].index(1)])

