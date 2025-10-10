# Desafio 059: Crie um programa que leia dois valores e mostre um menu. O programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

menu = '''
MENU:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair'''

opção = 0

while opção != 5:
    print("-"*38)
    print(f"{menu}")
    print("-"*38)
    opção = int(input(">>> Qual operação deseja realizar?: "))

    if opção == 1:
        print(f"{n1} + {n2} é igual à: {n1+n2}")
    
    elif opção == 2:
        print(f"{n1} x {n2} é igual à: {n1*n2}")

    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior número entre {n1} e {n2} é: {maior}")
    
    elif opção == 4:
        print("-"*38)
        print("Informe os números novamente. ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    sleep(2)

print("Programa Encerrado!")
