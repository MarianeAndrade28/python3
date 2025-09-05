# Desafio 020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
aluno1 = input("1º Aluno: ")
aluno2 = input("2º Aluno: ")
aluno3 = input("3º Aluno: ")
aluno4 = input("4º Aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print(f"A ordem de apresentação será: {lista}")