# Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print(f"O dobro de {numero} é igual à: {dobro}")
print(f"O triplo de {numero} é igual à: {triplo}")
print(f"A raiz quadrada de {numero} é igual à: {raiz:.2f}")
