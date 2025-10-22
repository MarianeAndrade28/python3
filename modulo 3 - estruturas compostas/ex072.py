# Desafio 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        try:
            print('-'*35)
            num = int(input("Digite um número entre 0 e 20: "))
        except ValueError:
            print("Comando Inválido! Digite um número inteiro.")
            continue

        if 0 <= num <= 20:
            break

        print("Comando Inválido! Tente Novamente.")

    print(f"Você digitou o número {cont[num]}")

    while True:
        print('-'*35)
        pergunta = str(input("Deseja continuar?: [S/N] ")).strip().upper()[0]

        if pergunta in 'SN':
            break

        print("Comando Inválido! Tente Novamente.")

    if pergunta == 'N':
        break

print("Programa Encerrado...")
