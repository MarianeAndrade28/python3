# Desafio 058: Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

palpites = 0

from random import randint
computador = randint(0, 10)
print("-"*6, "VAMOS JOGAR?", "-"*6)
print("Sou o seu computador...")
print("Será que você consegue adivinhar o número que estou pensando?: ")
print("-"*65)

acertou = False

while not acertou:
    resp = int(input("Qual é o seu palpite? "))
    if resp > computador:
        print("Menos...Tente novamente")
        palpites += 1

    elif resp < computador:
        print("Mais...Tente novamente")
        palpites += 1
    else:
        print("Você Acertou!")
        acertou = True
        palpites += 1

print(f"Número de tentativas: {palpites}")
