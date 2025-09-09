# Desafio 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza -> Primeiro: Ana, Último: Souza.

n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()

print(f"Muito prazer em conhecê-lo!\nSeu primeiro nome é {nome[0]}.\nSeu último nome é {nome[-1]}")
