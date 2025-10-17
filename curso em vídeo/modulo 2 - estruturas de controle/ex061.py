# Desafio 061: Refaça o desafio 051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros termos dela, desta vez usando a estrutura WHILE.

print("="*6, "GERADOR DE PA", "="*6)
termo1 = int(input("Primeiro termo: "))
razão = int(input("Razão: "))

termo = termo1
contador = 1

while contador <= 10:
    print(f"{termo} -> ", end='')
    termo += razão
    contador += 1
print("FIM!")
