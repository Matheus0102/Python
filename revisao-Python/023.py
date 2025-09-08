'''
Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:
Apenas os 3 primeiros mais assistidos
Os últimos 2 mais assistidos
A lista em ordem alfabética
Em que posição está “O rei leão”
'''

filmes = ('Avatar', 'Vingadores', 'Avatar: O caminho da Água', 'Titanic', 'Ne Zhe 2', 'Star wars: O despertar da força', 'Vingadores: Guerra Infinita', 'Homem-Aranha: Sem Volta para Casa', 'Divertida Mente 2', 'Jurassic World', 'O Rei Leão')

for cont in range(1):
    print(f'Os três primeiros filmes mais assistidos são: {filmes[0:3]}')

filmes_invertida = tuple(reversed(filmes))

for cont in range(1):
    print(f'Os dois ultimos filmes mais assistidos são: {filmes_invertida[0:2]}')

filmes_ordenada = sorted(filmes)
print(f'A lista em ordem alfabética: {filmes_ordenada}')

indice_filme = filmes.index('O Rei Leão')
print(f'O filme "O rei leão" se encontra na posição: {indice_filme + 1}')






