# Desafio 019: Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno1 = input("1º Aluno: ")
aluno2 = input("2º Aluno: ")
aluno3 = input("3º Aluno: ")
aluno4 = input("4º Aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)

print(f"O aluno escolhido foi: {escolhido}")
