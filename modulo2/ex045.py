# Desafio 045: Crie um programa que faça o computador jogar JOKENPÔ com você.

from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print("""
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

try:
    jogador = int(input("Qual é a sua jogada? "))
    if jogador not in [0, 1, 2]:
        print("OPÇÃO INVÁLIDA!")
    
    else:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PÔ")

        print("-"*30)
        print(f"Computador jogou: {itens[computador]}")
        print(f"Você jogou: {itens[jogador]}")
        print("-"*30)

        if computador == jogador:
            print("EMPATE!")
        elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
            print("VITÓRIA DO JOGADOR!")
        else:
            print("VITÓRIA DO COMPUTADOR!")

except ValueError:
    print("OPÇÃO INVÁLIDA! DIGITE APENAS: 0, 1 OU 2.")
