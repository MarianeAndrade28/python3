# Desafio 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

leia = input("Digite algo: ")
print("O tipo primitivo desse valor é:", type(leia))
print("Só tem espaços?", leia.isspace())
print("É um número?", leia.isnumeric())
print("É alfabético?", leia.isalpha())
print("É alfanumérico?", leia.isalnum())
print("Está em letras maiúsculas?", leia.isupper())
print("Está em letras minúsculas?", leia.islower())
print("Está capitalizada?", leia.istitle())
