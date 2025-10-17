# Desafio 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (int) e o programa vai informar quantas cédulas de cada valor será entregue.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print("-"*35)
print(f"{'BANCO ANDRADE':^35}")
print("-"*35)

valor = int(input("Valor do saque: R$"))
totalSaque = valor
cedulaAtual = 50
totCedulas = 0

while True:
    if totalSaque >= cedulaAtual:
        totalSaque -= cedulaAtual
        totCedulas += 1
    
    else:
        if totCedulas > 0:
            print(f"Total de {totCedulas} cédulas de R${cedulaAtual}")

        if cedulaAtual == 50:
            cedulaAtual = 20

        elif cedulaAtual == 20:
            cedulaAtual = 10
        
        elif cedulaAtual == 10:
            cedulaAtual = 1
        
        totCedulas = 0

        if totalSaque == 0:
            break

print("-"*35)
print("Agradecemos à preferência. Volte sempre!")
