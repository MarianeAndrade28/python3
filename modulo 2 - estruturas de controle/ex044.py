# Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2x no cartão: Preço normal;
# 3x ou mais no cartão: 20% de juros;
# À vista no cartão: 5% de desconto.

print("="*8, "LOJAS ANDRADE", "="*8)
preco = float(input("Preço das compras: R$ "))

print("""
FORMAS DE PAGAMENTO:
[1] À vista dinheiro/chque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")

print("-"*30)
pagamento = int(input("Qual a sua opção?: "))

if pagamento == 1:
    preco_final = preco - (preco * 0.1)
    print(f"Valor da compra: R${preco_final:.2f} à vista, com 10% de desconto.")

elif pagamento == 2:
    preco_final = preco - (preco * 0.05)
    print(f"Valor da compra: R${preco_final:.2f} no cartão, com 5% de desconto.")

elif pagamento == 3:
    preco_final = preco / 2
    print(f"Compra parcelada em 2x de R${preco_final:.2f} SEM JUROS.")

elif pagamento == 4:
    parcelas = int(input("Quantas parcelas?: "))
    preco_final = (preco * 0.2) + preco
    print(f"Sua compra será parcelada em {parcelas}x de {(preco_final/parcelas):.2f} COM JUROS.")
    print(f"Preço final da sua compra: R${preco_final:.2f}")

else:
    print(f"ERRO: Opção Inválida. Tente novamente!")
    print(f"Preço final da sua compra: R${preco:.2f}")

