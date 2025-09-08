'''
# Operações em Python

print(1 + 1)
print(2 - 6)
print(60000/3)
print(99875 * 56)
print(2 ** 3)

# Texto
print('Olá Mundo!')

#Variáveis
a = 5
b = 4
print(a + b)
print(a - b)
c = (a + b) / 5
print(c)

#print formatado
print(f'A soma de a e b é {c}')

#Entrada de dados
nome = input('Digite o nome: ')
idade = input('Digite a sua idade: ')

print(f'Seu nome é {nome} e você tem {idade} anos')

#Inteiro
idade_joao = int(input('João, quantos anos você tem? '))
idade_felipe = int(input('Felipe, quantos anos você tem? '))

soma_idades = idade_joao + idade_felipe

print(f'A soma das idades é {soma_idades}')

#Strings
Nome = 'Luis Eulálio'
#Fatiamento
print(Nome[0])
print(Nome[3:7])

#transformação
print(Nome.upper())
print(Nome.lower())
print(len(Nome))

#Contar
print(Nome.count('a'))
Nome = Nome.replace('l', 'p')
print(Nome)

Nome = input('Digite seu nome: ').strip()
print(Nome)

Nome = input('Digite seu nome: ').split()
print(Nome)
print(Nome[0])

#Find
frase = input('Digite a sua frase: ')
print(frase.find('e'))
print(frase.rfind('e'))



#Condicionais
altura = float(input('Digite a sua altura: '))

#1
if altura > 3:
    print('Cuidado!! Vai bater a cabeça :/ ')
else:
    print('Pode andar no brinquedo')

#2
if altura > 3:
    print('Cuidado!! Vai bater a cabeça :/ ')

elif altura < 1:
    print('Quem sabe ano que vem! ')

else:
    print('Pode andar no Brinquedo')

#E
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))

if altura > 1 and idade > 14:
    print('Você pode andar')
else:
    print('Quem sabe ano que vem')


import random

aleatorio = random.randint(1,10)
print(aleatorio)


for ele in range(0, 1000):
    print("*")

for ele in range(0,10):
    print(ele)

for ele in range(0,10,2):
    print(ele)

for ele in range(10, 0, -1):
    print(ele)

soma = 0
for ele in range(0,11):
    soma = soma + ele


#while

contador = 0

while contador < 100:
    print('Oi')
    contador += 1


# Strings
resposta = ''

while resposta != 'N':
    print('Seja bem vindo')
    resposta = input('Deseja continuar? [S/N]: ').strip().upper()[0]


menu = ''

while menu != 4:
    menu = int(input('Digite o menu:'
                     '\n1. Novos Valores'
                     '\n2. Área'
                     '\n3. Volume '
                     '\n4. Sair -> '))

    if menu == 1:
        raio = float(input('Digite o raio: '))

    elif menu == 2:
        print(f'A área é {3.1415 * raio ** 2}')

    elif menu == 3:
        print(f'O volume é {(4/3)* 3.1415 * raio ** 3}')

while True:
    n = input('digite um número[0000 para sair]: ')

    if n == '0000':
        break

while True:
    try:
        numero = int(input('Digite um numero: '))
        x = 10 / 0

    except ValueError:
        print('Só aceitamos números')
    except ZeroDivisionError:
        print('Cuidado ao dividir por 0 ')
    except:
        print('Erro não documentado')


def mensagem_boas_vindas():
    print('------------------ OOIIIIII ---------------------------')

def mensagem_personalizada(msg):
    print('----------------')
    print(msg)
    print('----------------')

def area_esfera(raio):
    A = (4 * raio ** 2 * 3.1415)
    return A

#1 Caso
mensagem_boas_vindas()

# 2 Caso
nome = input('Digite seu nome: ')
mensagem_personalizada(nome)

# 3 Caso
Area_Esfera_1 = area_esfera(3)
Area_Esfera_2 = area_esfera(6)

print(Area_Esfera_1)


#Tuplas
carro = ('Ferrari', 'Vermelha', '2023')

print(carro)

for ele in carro:
    print(ele)

for cont in range(0, len(carro)):
    print(carro[cont])


b = (1,2,3)
a = (4,5,6)
c = a + b

print(c)
print(sorted(c))
# Posição
print(c.index(3))

# Listas

Nomes = ['João', 'Camila', 'Armando', 'Raskolnikov', 'Felipe']
Nomes[0] = 'Gustavo'
Nomes.insert(3, 'Thiago')
Nomes.append('Karina')

print(Nomes)

nomes = []

for ele in range(5):
    nomes.append(input('Digite seu nome: '))

print(nomes)


Idades = [5, 4, 3, 2, 1]

print(sum(Idades))
print(len(Idades))
print(f'A média é {sum(Idades) / len(Idades)}')
print(max(Idades))
print(min(Idades))


Gastos_Fevereio = [2,3,4,5,6,7]
Gastos_Janeiro  = [1,2,3,4,5,6]

Soma_geral = []
for ele in range(0, len(Gastos_Fevereio)):
    Soma_geral.append(Gastos_Fevereio[ele] + Gastos_Janeiro[ele])

print(Soma_geral)
print(sum(Gastos_Fevereio) + sum(Gastos_Janeiro))

# Listas Aninhadas

Alunos = []
dados = []

for x in range(3):
    dados.append(input('Digite o seu nome: '))
    dados.append(int(input('Digite a sua idade: ')))
    Alunos.append(dados[:])
    dados.clear()

print(Alunos)

Alunos = []
nomes = []
idades = []

for x in range(3):
    nomes.append(input('Digite o seu nome: '))
    idades.append(int(input('Digite a sua idade: ')))

Alunos.append(nomes[:])
Alunos.append(idades[:])

print(Alunos)


bd = [['Felipe', 'Armando', 'Clarice'], [19, 8, 6]]
print(bd[0])
print(bd[1])
print(bd[0][0])
print(bd[1][0])

for ele in bd[0]:
    print(ele)

carro = {}
concessionaria = []

for c in range(0, 3):
    carro['nome'] = str(input('Nome do Carro '))
    carro['ano'] = int(input('Ano do Carro '))
    concessionaria.append(carro.copy())
    print(concessionaria)


concessionaria = {}
carro_nome = []
carro_ano = []

for i in range(3):
    carro_nome.append(input('Nome: '))
    carro_ano.append(int(input('Ano: ')))

concessionaria['Nome'] = carro_nome[:]
concessionaria['Ano'] = carro_ano[:]

print(concessionaria)

concessionaria = {'Nome': ['a', 'b', 'c'], 'Ano': [2000, 2001, 2002]}

print(concessionaria.values())
print(concessionaria.keys())
print(concessionaria.items())
print(concessionaria)

'''
