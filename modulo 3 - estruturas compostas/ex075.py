# Desafio 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9; b) Em que posição foi digitado o primeiro valor 3; c) Quais foram os números pares.

num = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")))

print(f"Você digitou os valores: {num}")
print(f"O número 9 apareceu {num.count(9)} vezes")

if 3 in num:
    print(f"O número 3 apareceu na {num.index(3)+1}ª posição")
else:
    print("O número 3 não aparece em nenhuma posição.")
print(f"Os números pares digitados foram: ", end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')
