# Desafio 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f"Qual o peso(Kg) da {p} pessoa?: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("-"*40)
print(f"O MAIOR peso registrado foi de: {(maior):.1f} Kg")
print(f"O MENOR peso registrado foi de: {(menor):.1f} Kg")
