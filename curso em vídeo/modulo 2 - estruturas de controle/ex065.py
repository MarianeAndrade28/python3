# Desafio 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = 0
maior = 0
menor = 0
quantidade = 0
pergunta = 'S'

while pergunta in 'Ss':
    try:
        num = int(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue
    
    soma += num
    quantidade += 1

    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    pergunta = str(input("Deseja continuar? [S/N] ")).strip()[0].upper()

    while pergunta not in 'SN':
        print("Comando Inválido! Digite apenas S ou N.")
        pergunta = str(input("Deseja continuar? [S/N] ")).strip()[0].upper()

if quantidade > 0:
    media = soma / quantidade

    print("-"*40)
    print(f"Você digitou {quantidade} valores.")
    print(f"A soma entre todos os valores é igual à: {soma}")
    print(f"A média entre os valores é: {media:.2f}")
    print(f"O maior valor lido foi: {maior}")
    print(f"O menor valor lido foi: {menor}")
else:
    print("\nNenhum número foi inserido. Programa encerrado.")