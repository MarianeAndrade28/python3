# Desafio 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

titulo = "DEZ TERMOS DE UMA PA"
largura = 30

print("=" * largura)
print(f"{titulo:^30}")
print("=" * largura)

termo1 = int(input("Primeiro Termo: "))
razão = int(input("Razão: "))
decimo = termo1 + (10-1) * razão

for c in range(termo1, decimo + razão, razão):
    print(f"{c}", end=' -> ')
print("FIM!")
