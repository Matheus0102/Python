'''
Peça um texto ao usuário e uma palavra proibida.
Substitua todas as aparições da palavra proibida por "***" e exiba o texto censurado.
'''

texto = input("Digite um texto: ").lower().strip()
proibida = input("Digite a palavra proibida: ").lower().strip()

# Substitui todas as ocorrências da palavra proibida por ***
texto_censurado = texto.replace(proibida, "***")

print("\n🛑 Texto censurado:")
print(texto_censurado)
