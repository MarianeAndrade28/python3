# Desafio 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
# Qual é o total gasto na compra;
# Quantos produtos custam mais de R$1000;
# Qual é o nome do produto mais barato.

totCompra = totMil = menor = cont = 0
barato = ' '

while True:
    produto = str(input("Nome do Produto: "))
    preço = float(input("Preço: R$ "))
    cont += 1
    totCompra += preço

    if preço > 1000:
        totMil += 1
    
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Deseja continuar?: [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break

print("-"*10, "FIM DO PROGRAMA", "-"*10)
print(f"Total da Compra: R${totCompra:.2f}")
print(f"Temos {totMil} produto(s) com valor superior à R$1000,00")
print(f"O produto mais barato foi {barato} custando R${menor:.2f}")
