print('Seja bem-vindo a minha loja')
preco = float(input('Digite o preço do produto: '))
qtd = int(input('Quantidade do produto: '))
total = preco * qtd
desconto = 0


#Programa Principal
if total >= 2500 and total < 6000:
   desconto = (4 / 100) * total
elif total >= 6000 and total < 10000:
       desconto = (7 / 100) * total
elif total >= 10000:
   desconto = (11 / 100) * total
else:
   print('Desconto indisponível para compras abaixo de R$2500 reais')


com_desconto = total - desconto #Valor total com desconto

print('-'*50)
print('O valor total sem desconto é de: R${:.2f}'.format(total))
print('O valor total com desconto é de: R${:.2f}'.format(com_desconto))
