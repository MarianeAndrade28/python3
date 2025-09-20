# Desafio 042: Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: Todos os lados iguais.
# ISÓSCELES: Dois lados iguais.
# ESCALENO: Todos os lados diferentes.

print("-="*20)
print("ANALISADOR DE TRIÂNGULOS")
print("-="*20)

a = float(input("Primeiro segmento: "))
b = float(input("Segmento segumento: "))
c = float(input("Terceiro segmento: "))

print("-="*20)
if (a + b) > c and (b + c) > a and (a + c) > b:
    print(f"Os segmentos acima PODEM FORMAR um Triângulo: ", end="")
    if a == b == c:
        print("EQUILÁTERO!")
    elif a != b != c != a:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print(f"Os segmentos acima NÃO PODEM FORMAR um Triângulo!")
