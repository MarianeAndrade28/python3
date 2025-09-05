# Desafio 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual é o salário do funcionário? R$"))
aumento = salario + (salario * 0.15)

print(f"O funcionário que recebia R${salario:.2f}, passará a receber R${aumento:.2f} com o aumento de 15% do seu salário.")
