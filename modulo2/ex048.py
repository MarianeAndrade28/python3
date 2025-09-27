# Desafio 048: Faça um programa que calcule a soma entre todas os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 # acumulador
contador = 0 # contador

for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c

print(f'A soma de todos os {contador} valores é igual à: {soma}')
