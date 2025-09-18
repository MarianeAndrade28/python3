# Desafio 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO!
# Média entre 5.0 e 6.9: RECUPERAÇÃO!
# Média 7.0 ou superior: APROVADO!

n1 = float(input("Nota avaliação 1: "))
n2 = float(input("Nota avaliação 2: "))
media = (n1 + n2) / 2

print(f"Com as notas {n1} e {n2}, sua média será {media}")
if media >= 7:
    print("Parabéns! Você foi APROVADO.")
elif media < 5:
    print("Você foi REPROVADO!")
elif media >= 5 <= 6.9:
    print("RECUPERAÇÃO!")
