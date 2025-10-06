# Desafio 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0


for pessoas in range(1,8):
    nascimento = int(input(f"Em que ano a {pessoas}ª pessoa nasceu?: "))
    idade = ano_atual - nascimento

    if idade >= 21:
        totmaior += 1

    else:
        totmenor += 1


print(f"No total foram {totmaior} pessoas MAIORES de idade.")
print(f"E {totmenor} pessoas MENORES de idade.")
