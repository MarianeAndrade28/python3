# Desafio 017: Faça um programa que leia o comprimento do Cateto Oposto e do Cateto Adjacente de um triângulo retângulo, calcule e mostre o comprimento da Hipotenusa.

from math import sqrt
catetoOposto = float(input("Comprimento do Cateto Oposto: "))
catetoAdjacente = float(input("Comprimento do Cateto Adjacente: "))
hipotenusa = (catetoOposto ** 2) + (catetoAdjacente ** 2)

print(f"A Hipotenusa vai medir: {sqrt(hipotenusa):.2f}")
