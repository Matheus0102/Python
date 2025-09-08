'''
Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes das duas
listas. Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].
'''

lista_1 = []
lista_2 = []

for i in range(5):
    try:
        lista_1.append(int(input('N: ')))
        lista_2.append(int(input('N: ')))
    except:
        print('Apenas numeros: ')

lista_3 = []
for i in range(5):
    lista_3.append(lista_1[i] + lista_2[i])

print(lista_3)