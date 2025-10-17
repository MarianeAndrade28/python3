# Desafio 033: Faça um programa que leia três número e mostre na tela qual é o MAIOR e qual é o MENOR entre eles.

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
lista = [n1, n2, n3]

print(f"Os números digitados foram: {lista}")
print(f"O MAIOR número entre eles é: {max(lista)}")
print(f"O MENOR número entre eles é: {min(lista)}")
