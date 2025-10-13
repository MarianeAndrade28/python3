# Desafio 063: Escreva um programa que leia um número inteiro qualquer e mostre na tela os n primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.

print("="*4, "SEQUÊNCIA DE FIBONACCI", "="*4)

n = int(input("Quantos termos?: "))
t1 = 0
t2 = 1

print(f"{t1} -> {t2}", end='')
contador = 3

while contador <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end='')
    t1 = t2
    t2 = t3
    contador += 1
print(" -> FIM!")
