# Desafio 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input("Nota em Português: "))
nota2 = float(input("Nota em Matemática: "))
media = (nota1 + nota2) / 2

print(f"Sua média é: {media:.1f}")
