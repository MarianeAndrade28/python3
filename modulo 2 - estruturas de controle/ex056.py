# Desafio 056: Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo; Quem é o homem mais velho; Quantas mulheres tem menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_hom = 0
mais_velho = ''
total_mulher20 = 0

for p in range(1, 5):
    print('-'*6, f'{p}ª PESSOA', '-'*6)
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_hom:
            maior_idade_hom = idade
            mais_velho = nome
    
    if sexo == 'F' and idade < 20:
        total_mulher20 += 1


media_idade = soma_idade / 4

print("-"*20)
print(f"A média de idade deste grupo é de: {media_idade:.1f} anos")
print(f"O homem mais velho tem {maior_idade_hom} anos e se chama {mais_velho}")
print(f"Ao todo temos {total_mulher20} mulher(es) com menos de 20 anos")
