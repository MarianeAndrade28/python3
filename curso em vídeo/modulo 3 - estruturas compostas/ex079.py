# Desafio 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será acionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    try:
        valor = input('Digite um valor: ')
        num = int(valor)

        if num in lista:
            print(f'ERRO: Valor {num} Duplicado! Tente outro número.')
            continue

        lista.append(num)
        print(f'Valor {num} adicionado com sucesso!')

        resp = input('Quer continuar?: [S/N] ').strip().lower()

        if resp == 's':
            continue
        elif resp == 'n':
            break
        else:
            print('Resposta Inválida! Tente novamente.')
            continue

    except ValueError:
        print(f'ERRO: Por favor, digite um número inteiro')

if lista:
    lista.sort()
    print(f'\nLista: {lista}')
