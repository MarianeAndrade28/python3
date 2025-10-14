# Desafio 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vitorias = 0

while True:

    print("="*6, "PAR OU ÍMPAR", "="*6)

    jogador = int(input("Digite um valor: "))
    computador = randint(0, 11)
    total = jogador + computador
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total igual à: {total} ->", end=" ")
    print("Deu PAR" if total % 2 == 0 else "Deu ÍMPAR")
    
    print("-"*50)
    if escolha == 'P':
        if total % 2 == 0:
            print("Você VENCEU!")
            vitorias += 1
        else:
            print("Você PERDEU!")
            break

    elif escolha == 'I':
        if total % 2 == 1:
            print("Você VENCEU!")
            vitorias += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar de novo?")
    print("-"*50)

print(f"GAME OVER! Total de Vitórias: {vitorias}")
