# Desafio 037: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário.
# 2 para octal.
# 3 para hexadecimal.

import math
numero = int(input("Digite um número inteiro: "))
print("="*15, "MENU", "="*15)
print("""Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL""")
print("="*36)

opcao = input("Sua opção: ")

if opcao == "1":
    print(f"O número {numero} convertido para BINÁRIO é igual à: {bin(numero)[2:]}")
elif opcao == "2":
    print(f"O número {numero} convertido para OCTAL é igual à: {oct(numero)[2:]}")
elif opcao == "3":
    hex(numero)
    print(f"O número {numero} convertido para HEXADECIMAL é igual à: {hex(numero)[2:]}")
else:
    print("OPÇÃO INVÁLIDA!")
