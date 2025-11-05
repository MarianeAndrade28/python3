# Desafio 080: Crie um program onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for c in range(0, 5):
    n = int(input("Digite um valor: "))

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista')
                break
            pos += 1

print('-'*50)
print(f"Os valores digitados foram: {lista}")
