# Desafio 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9; b) Em que posição foi digitado o primeiro valor 3; c) Quais foram os números pares.

num = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")))
print(f"Você digitou os valores: {num}")
