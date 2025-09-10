# Desafio 031: Desenvolva um programa que a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input("Qual a distância da viagem?: "))

if distancia <= 200:
    print(f"A passagem para uma viagem de {distancia:.1f}Km custará R${distancia*0.50:.2f}")
else:
    print(f"A passagem para uma viagem de {distancia:.1f}Km custará R${distancia*0.45:.2f}")
