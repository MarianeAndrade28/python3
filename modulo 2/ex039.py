# Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
atual = date.today().year
nascimento = int(input("Ano de Nascimento: "))
idade = atual - nascimento

print(f"Nascidos em {nascimento} tem {idade} anos agora")

if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE!")
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f"Você já deveria ter se alistado a {saldo} anos.")
    print(f"Seu alistamento foi em {ano}")

elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f"Você ainda não tem 18 anos. Faltam {saldo} anos para o seu alistamento.")
    print(f"Seu alistamento será em {ano}")
