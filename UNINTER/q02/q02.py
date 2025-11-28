print('Seja bem-vindo a minha gelateria')
#Cardápio
print('-' * 25,'CARDÁPIO','-' * 25)
print('-' * 6,"|   TAMANHO   |   CUPUAÇU (CP)   |   AÇAÍ (AC)  |",'-' * 6)
print('-' * 6,"|      P      |      R$ 9,00     |   R$ 11,00   |",'-' * 6)
print('-' * 6,"|      M      |     R$ 14,00     |   R$ 16,00   |",'-' * 6)
print('-' * 6,"|      G      |     R$ 18,00     |   R$ 20,00   |",'-' * 6)
print('-' * 60)


#Sabores
'AÇAÍ (AC)'
'CUPUAÇU (CP)'
CP = {'P': 9.00, 'M': 14.00, 'G': 18.00} #Cupuaçu
AC = {'P': 11.00, 'M': 16.00, 'G': 20.00} #Açaí
total = 0 #Acumulador


#Programa Principal
while True:
   sabor = input('Escolha o sabor desejado (AC/CP): ')
   if sabor not in ('AC', 'CP'):
       print('Sabor inválido. Tente novamente')
       continue
   tamanho = input('Escolha o tamanho (P,M,G): ')
   if tamanho not in ('P', 'M', 'G'):
       print('Tamanho inválido. Tente novamente')
       continue

   print('-'*50)
   if sabor == 'AC':
       total += AC[tamanho]
       print('Você escolheu AÇAÍ tamanho {}.'.format(tamanho))
   elif sabor == 'CP':
       total += CP[tamanho]
       print('Você escolheu CUPUAÇU tamanho {}.'.format(tamanho))


   res = input('Deseja pedir mais alguma coisa? (S/N): ') #Pergunta
   if res != 'S':
       break

print('-'*50)
print('Total a pagar: R${:.2f}'.format(total))
