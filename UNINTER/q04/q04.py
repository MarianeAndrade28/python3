print('Seja bem-vindo ao meu controle de livros')

#Cadastro de livro
def cadastrar_livro():
   print('-' * 40)
   print('MENU - CADASTRAR LIVROS')
   print('-' * 40)
   nome = input('Nome do livro: ')
   autor = input('Autor do livro: ')
   editora = input('Editora do livro: ')
   livro = {'id': len(lista_livro) + 1, 'nome': nome, 'autor': autor, 'editora': editora}
   lista_livro.append(livro)


def menuConsultar_livro():
   print('-' * 40)
   print('MENU - CONSTULTAR LIVROS')
   print('-' * 40)
   print('1 - Consultar Todos')
   print('2 - Consultar por ID')
   print('3 - Consultar por Autor')
   print('4 - Retornar ao Menu Principal')


def consultar_todos():
   print('-' * 40)
   print('LISTA DE LIVROS')
   print('-' * 40)
   for livro in lista_livro:
       print('ID:', livro['id'])
       print('Nome:', livro['nome'])
       print('Autor:', livro['autor'])
       print('Editora:', livro['editora'])
       print('-' * 30)


def consultar_id():
   id_consulta = int(input('Digite o ID do livro desejado: '))
   encontrado = False
   for livro in lista_livro:
       if livro['id'] == id_consulta:
           print('ID:', livro['id'])
           print('Nome:', livro['nome'])
           print('Autor:', livro['autor'])
           print('Editora:', livro['editora'])
           print('-' * 30)
           encontrado = True
           break
   if not encontrado:
       print('Livro não encontrado, ID {} inválido.'.format(id_consulta))


def consultar_autor():
   autor_consulta = input('Digite o nome do autor do livro: ')
   encontrado = False
   for livro in lista_livro:
       if livro['autor'] == autor_consulta:
           print('ID:', livro['id'])
           print('Nome:', livro['nome'])
           print('Autor:', livro['autor'])
           print('Editora:', livro['editora'])
           print('-' * 30)
           encontrado = True
   if not encontrado:
       print('Nenhum livro com o autor {} foi encontrado.'.format(autor_consulta))
def servico_ofe(pergunta,min,max):
   while True:
       try:
           op = int(input(pergunta))
           if (min <= op <= max):
               return op
           else:
               print('Opção Inválida. Tente novamente')
       except ValueError:
           print('Por favor, insira um número válido')


def remover_livro():
   nome_livro = input('Nome do livro que deseja remover: ')
   livro_removido = False
   for livro in lista_livro:
       if livro['nome'] == nome_livro:
           lista_livro.remove(livro)
           print('O livro {} foi deletado com sucesso.'.format(nome_livro))
           livro_removido = True
           break
   if not livro_removido:
       print('O livro {} não foi encontrado na lista.'.format(nome_livro))


lista_livro = []


#Programa Principal
while True:
   print('-' * 40)
   print('MENU PRINCIPAL')
   print('-' * 40)
   print('1 - Cadastrar Livro')
   print('2 - Consultar Livro')
   print('3 - Remover Livro')
   print('4 - Encerrar Programa')


   op = servico_ofe('Escolha a opção desejada: ',1,4)
   if op == 1:
       cadastrar_livro()
   elif op == 2:
       menuConsultar_livro()  # Menu secundário
       consulta_op = servico_ofe('Escolha a opção desejada: ', 1, 4)
       if consulta_op == 1:
           consultar_todos()
       elif consulta_op == 2: # Código para consultar por ID
           consultar_id()
       elif consulta_op == 3: # Código para consultar por autor
           consultar_autor()
       elif consulta_op == 4:
           continue
       else:
           print('Opção Inválida')
   elif op == 3:
       remover_livro()
   else:
       print('Programa encerrado.')
       break
