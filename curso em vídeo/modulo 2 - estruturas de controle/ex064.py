# Desafio 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

from time import sleep
soma = 0
contador = 0
num = 0

while num != 999:
    num = int(input("Digite um número (ou 999 para sair): "))
    
    if num != 999:
        soma += num
        contador += 1

print("-"*40)
print("FINALIZANDO...")
sleep(1)
print(f"Números digitados: {contador}")
print(f"A soma entre eles foi de: {soma}")
