# Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Aqueles com valor superior à R$1.250,00 recebem aumento de 10%.
# Já os inferiores ou iguais, recebem aumento de 15%.

salario = float(input("Qual é o salário do funcionário?: R$"))

if salario <= 1250:
    print(f"Quem recebia R${salario:.2f}, passa a receber R${(salario*0.15)+salario:.2f}") #Salário novo com 15% de aumento
else:
    print(f"Quem recebia R${salario:.2f}, passa a receber R${(salario*0.10) + salario:.2f}") #Salário novo com 10% de aumento
