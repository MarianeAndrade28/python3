# Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Qual o valor da casa?: R$ "))
salario = float(input("Salário do comprador?: R$ "))
anos = int(input("Quantos anos de financiamento?: "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f"Uma casa no valor de R${casa:.2f}, financiada em {anos} anos, terá a mensalidade no valor de R${prestacao:.2f}")

if prestacao <= minimo:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO!")
