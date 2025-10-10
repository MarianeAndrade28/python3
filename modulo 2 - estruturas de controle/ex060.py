# Desafio 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5 -> 5x4x3x2x1 = 120

from math import factorial
num = int(input("Digite um número: "))
c = num

print(f'>>> Fatorial de {num}! = ', end='')
while c > 0:
    print(f"{c}", end='')
    print(" x " if c > 1 else ' = ', end='')
    c -= 1
print(f"{factorial(num)}")
