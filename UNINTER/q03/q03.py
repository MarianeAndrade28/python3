print('Seja bem-vindo a minha copiadora')

#Funções:
def escolha_servico(pergunta,min,max):
   while True:
       try:
           x = int(input(pergunta))
           if min <= x <= max:
               return x
           else:
               print('Serviço inválido. Escolha um número entre {} e {}'.format(min,max))
       except ValueError:
           print('Por favor, insira um número inteiro.')


def servico_extra(pergunta,min,max):
   while True:
       try:
           x = int(input(pergunta))
           while x < min or x > max:
               print('Escolha inválida. Tente novamente')
               continue
           return x
       except ValueError:
           print('Por favor, insira um número inteiro.')


def num_pagina(pergunta, min, max):
   while True:
       try:
           x = int(input(pergunta))
           if min <= x <= max:
               return x
           else:
               print('Limite de páginas ultrapassado. Por favor, insira um número entre {} e {}'.format(min,max))
       except ValueError:
           print('Por favor, insira um número inteiro')


#Programa Principal
while True:
#Serviços Comuns
   print('-'*50)
   print('Serviços:')
   print('1 - Digitalização (DIG) - R$1,10')
   print('2 - Impressão Colorida (ICO) - R$1,00')
   print('3 - Impressão Preto e Branco (IBO) - R$0,40')
   print('4 - Fotocópia (FOT) - R$0,20')


   servico = escolha_servico('Escolha o serviço desejado: ',1,4)


#Serviço Extra
   print('-'*50)
   print('Serviço adicional')
   print('1 - Encadernação Simples - R$15,00')
   print('2 - Encadernação Capa Dura - R$40,00')
   print('0 - Não desejo mais nada')


   servico_extra = escolha_servico('Deseja adicionar mais algum serviço? ',0,2)
   op = num_pagina('Digite o número de páginas: ',1,20000)
   total = 0 #Acumulador


#Serviços Comuns
   if servico == 1:
       total += op * 1.10
   elif servico == 2:
       total += op * 1
   elif servico == 3:
       total += op * 0.40
   elif servico == 4:
       total += op * 0.20
   else:
       print('Serviço inválido')
       continue


#Serviço Extra
   if servico_extra == 1:
       total += 15
   elif servico_extra == 2:
       total += 40


#Desconto
   print('-'*50)
   if op <= 20:
       desconto = total
       print('Não há desconto')
       print('Você escolheu {} páginas.\nTotal a pagar: R${:.2f}'.format(op,total))
   elif op < 200:
       desconto = total * 0.15
       total_com_desconto = total - desconto
       print('Você escolheu {} páginas.\nTotal a pagar: R${:.2f}'.format(op, total_com_desconto))
   elif op < 2000:
       desconto = total * 0.2
       total_com_desconto = total - desconto
       print('Você escolheu {} páginas.\nTotal a pagar: R${:.2f}'.format(op, total_com_desconto))
   elif op < 20000:
       desconto = total * 0.25
       total_com_desconto = total - desconto
       print('Você escolheu {} páginas.\nTotal a pagar: R${:.2f}'.format(op, total_com_desconto))
   else:
       print('Não aceitamos pedidos nessa quantidade de páginas')
