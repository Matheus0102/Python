'''
Escreva um programa que crie um dicionário com as informações de 5 livros, como título, autor, ano de lançamento e
número de páginas. Em seguida, exiba apenas os autores dos livros.
'''

titulo = []
autor = []
ano_De_lancamento = []
numero_De_Paginas = []

df = {}

for i in range(5):

    titulo.append(input('Titulo: '))
    autor.append(input('Autor: '))
    try:
        ano_De_lancamento.append(int(input('Ano de Lançamento: ')))
        numero_De_Paginas.append(int(input('Quantidade de Páginas: ')))
    except:
        ano_De_lancamento.append(int(input('Apenas numero válidos, ano de Lançamento: ')))
        numero_De_Paginas.append(int(input('Apenas numero válidos, quantidade de Páginas: ')))

df['Titulo'] = titulo[:]
df['Autor'] = autor[:]
df['Ano de Lançamento'] = ano_De_lancamento[:]
df['Quantidade de Páginas'] = numero_De_Paginas[:]
print(df[1])

