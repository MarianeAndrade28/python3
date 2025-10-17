# Desafio 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]

while sexo not in 'MF':
    print("Comando Inválido! Tente Novamente.")
    sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()

print("-"*20)
print(f"Sexo {sexo} registrado com sucesso!")
