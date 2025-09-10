# Desafio 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
print("-="*30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-="*30)
jogador = int(input("Em qual número eu pensei?: "))
print("Analisando resposta...")
sleep(2)

print(f"Pensei no número: {computador}")
if jogador == computador:
    print("Você Acertou!")
else:
    print("Não foi dessa vez.")
