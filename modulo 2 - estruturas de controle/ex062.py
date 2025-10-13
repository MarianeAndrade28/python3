# Desafio 062: Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele digitar 0 (termos).

print("="*6, "GERADOR DE PA", "="*6)
termo1 = int(input("Primeiro termo: "))
razão = int(input("Razão: "))

termo = termo1
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{termo} -> ", end='')
        termo += razão
        contador += 1
    print("PAUSA")

    mais = int(input("Quantos termos deseja mostrar à mais?: "))
print("-"*65)
print("Programa Encerrado!")
print(f"Ao todo, foram mostrados {total} termos")
