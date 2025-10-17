# Desafio 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("-="*20)
print("ANALISADOR DE TRIÂNGULOS")
print("-="*20)

a = float(input("Primeiro segmento: "))
b = float(input("Segmento segumento: "))
c = float(input("Terceiro segmento: "))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print(f"Os segmentos acima PODEM FORMAR um Triângulo!")
else:
    print(f"Os segmentos acima NÃO PODEM FORMAR um Triângulo!")
