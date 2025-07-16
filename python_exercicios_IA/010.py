'''
Verifique se uma palavra ou frase é um palíndromo (ou seja, pode ser lida de trás para frente e continuar igual).
Exemplos de palíndromos:

"arara"

"socorram me subi no onibus em marrocos"

💡 Dica: Remover espaços e deixar tudo em minúsculo antes de comparar.
'''

frase = input("Digite uma palavra ou frase: ")

# Remove espaços e deixa tudo minúsculo
frase_formatada = frase.replace(" ", "").lower()

# Inverte a string
frase_invertida = frase_formatada[::-1]

# Verifica se é igual à original formatada
if frase_formatada == frase_invertida:
    print("✅ É um palíndromo!")
else:
    print("❌ Não é um palíndromo.")