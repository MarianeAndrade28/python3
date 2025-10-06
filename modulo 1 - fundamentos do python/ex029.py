# Desafio 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual é a velocidade atual do carro?: "))

if velocidade > 80:
    print("Você foi multado por excesso de velocidade!")
    multa = (velocidade - 80) * 7
    print(f"Valor à pagar: R${multa:.2f}")
else:
    print("Tenha um bom dia. Dirija com segurança!")
