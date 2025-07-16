'''
Desafio 1 — Contador de Vogais
Peça uma frase ao usuário e diga quantas vogais (a, e, i, o, u) ela tem.
Desconsidere acentos. A contagem não precisa ser diferenciada entre maiúsculas e minúsculas.
'''

frase = input("Digite uma frase: ")
vogais = "aeiou"
contador = 0

frase = frase.lower()

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase contém {contador} vogais.")
