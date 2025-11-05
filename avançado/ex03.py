# Exercício Módulo 7 - If

categoria = input('Categoria: ').lower()
produto = input('Nome do Produto: ').upper()
quantidade = input('Quantidade atual do produto: ')

if categoria and produto and quantidade:
    quantidade = int(quantidade)
    if categoria == 'alimento':
        if quantidade < 50:
            print(f'Solicitar {produto} à equipe de compras, temos apenas {quantidade} unidades em estoque')

    elif categoria == 'bebida':
        if quantidade < 75:
            print(f'Solicitar {produto} à equipe de compras, temos apenas {quantidade} unidades em estoque')

    else:
        if quantidade < 30:
            print(f'Solicitar {produto} à equipe de compras, temos apenas {quantidade} unidades em estoque')

    if categoria == 'limpeza':
        if quantidade < 30:
            print(f'Solicitar {produto} à equipe de compras, temos apenas {quantidade} unidades em estoque')

else:
    print('Por favor, preencha todos os campos')
