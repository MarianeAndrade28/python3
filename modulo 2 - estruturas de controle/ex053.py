# Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ").upper().strip())
palavras = frase.split()
tudo_junto = ''.join(palavras)
inverso = ''

for letra in range(len(tudo_junto) -1, -1, -1):
    inverso += tudo_junto[letra]
print(f"O inverso de {tudo_junto} é: {inverso}")

if inverso == tudo_junto:
    print("Está frase é um PALÍNDROMO!")
else:
    print("Está frase NÃO é um PALÍNDROMO!")
