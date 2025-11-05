# Exercício Módulo 7 - If

vendFunc1 = 1000
vendFunc2 = 770
vendFunc3 = 2700

if vendFunc1 >= 1000:
    print(f'O funcionário 1 recebeu {vendFunc1 * 0.1:.0f} de bônus')
if vendFunc2 >= 1000:
    bônus = vendFunc2 * 0.1
else:
    bônus = 0
print(f'O funcionário 2 recebeu {bônus:.0f} de bônus')

if vendFunc3 >= 1000:
    bônus = vendFunc3 * 0.1
else:
    bônus = 0
print(f'O funcionário 3 ganhou {bônus:.0f} de bônus')

