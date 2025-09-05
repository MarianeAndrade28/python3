# Desafio 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Qual é o preço do produto? R$"))
desconto = preco - (preco * 0.05)

print(f"O produto custava R${preco:.2f}, na promoção com o desconto de 5% ele custará R${desconto:.2f}")
