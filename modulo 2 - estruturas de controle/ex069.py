# Desafio 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# Quantas pessoas tem mais de 18 anos;
# Quantos homens foram cadastrados;
# Quantas mulheres tem menos de 20 anos.

tot18 = totH = totM20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    
    resposta = ' '
    while resposta not in "SN":
        resposta = str(input("Deseja continuar?: [S/N] ")).strip().upper()[0]
    if resposta == 'N':
        break

print("-"*55)
print(f"O número de pessoas maiores de 18 anos é: {tot18}")
print(f"O número de homens cadastrados é igual à: {totH}")
print(f"Ao todo, temos {totM20} mulher(es) com idade inferior a 20 anos")
