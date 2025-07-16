'''
Peça uma frase e diga quantas palavras ela tem.
Use o método .split() para isso.
'''

frase = input("Digite uma frase: ")

# Divide a frase em palavras usando espaços como separador
palavras = frase.split()

# Conta a quantidade de palavras
quantidade = len(palavras)

print(f"A frase contém {quantidade} palavras.")




