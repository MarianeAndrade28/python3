# Desafio 038: Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# O PRIMEIRO valor é maior
# O SEGUNDO valor é maior
# Não existe valor maior, os dois são iguais

v1 = int(input("Digite o PRIMEIRO valor: "))
v2 = int(input("Digite o SEGUNDO valor: "))

if v1 > v2:
    print("O PRIMEIRO valor é MAIOR")
elif v2 > v1:
    print("O SEGUNDO valor é MAIOR")
else:
    print("Os dois valores são IGUAIS")
