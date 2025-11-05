# Desafio 078: Faça um program que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas respectivas POSIÇÕES na lista.

lista = []
print('-'*40)
for p in range(0, 5):
    try:
        valor = int(input(f'Digite um valor para a {p}ª posição: '))
        lista.append(valor)
    
    except ValueError:
        print('Erro: Digite um número inteiro')

print('-'*40)
print(f'\nVocê digitou os valores: {lista}')

if lista:
    valor_max = max(lista)
    valor_min = min(lista)

    pos_max = []
    pos_min = []

    for v, valor in enumerate(lista):
        if valor == valor_max:
            pos_max.append(v)
        if valor == valor_min:
            pos_min.append(v)

    print(f'O MAIOR valor digitado foi {valor_max} nas posições: {pos_max}')
    print(f'O MENOR valor digitado foi {valor_min} nas posições: {pos_min}')

else:
    print('Nenhum valor válido foi digitado!')
