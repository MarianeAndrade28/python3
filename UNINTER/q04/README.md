# 📝 Questão 4
Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de pessoas. Este software deve ter o seguinte menu e opções:
* Cadastrar Livro;
* Consultar Livro;
  * Consultar Todos; 
  * Consultar por Id;
  * Consultar por Autor;
  * Retornar ao Menu;
* Remover Livro;
* Encerrar Programa;
<br>

**Elabore um programa em Python que:**
1. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome `[EXIGÊNCIA DE CÓDIGO 1 de 8]`;
2. Deve-se implementar uma lista vazia com o nome de `lista_livro` e a variável `id_global` com valor inicial igual a 0 `[EXIGÊNCIA DE CÓDIGO 2 de 8]`;
<br>

3. Deve-se implementar uma função chamada `cadastrar_livro(id)` em que: `[EXIGÊNCIA DE CÓDIGO 3 de 8]`;
   * Pergunta **nome**, **autor**, **editora** do livro;
   * Armazena o **id** (este é fornecido via parâmetro da função), **nome**, **autor**, **editora** dentro de um dicionário;
   * Copiar o dicionário para dentro da `lista_livro`;
<br>

4. Deve-se implementar uma função chamada `consultar_livro()` em que: `[EXIGÊNCIA DE CÓDIGO 4 de 8]`;
   * Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu) e   printar a “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 :
        * Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados;
        * Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados;
        * Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados cadastrados;
        * Se Retornar ao menu, deve-se retornar ao menu principal;
<br>

5. Deve-se implementar uma função chamada `remover_livro()` em que: `[EXIGÊNCIA DE CÓDIGO 5 de 8]`;
   * Deve-se pergunta pelo **id** do colaborador a ser removido;
   * Remover o livro da `lista_livro`;
<br>

6. Deve-se implementar uma estrutura de menu no main em que: `[EXIGÊNCIA DE CÓDIGO 6 de 8]`;
   * Deve-se pergunta qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa)e executar o printar de “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 :
        * Se Cadastrar Livro, acrescentar em um `id_ global` e chamar a função `cadastrar_livro(id_ global)`;
        * Se Consultar Livro, chamar função `consultar_livro()`;
        * Se Remover Livro, chamar função `remover_livro()`;
        * Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
<br>

7. Deve-se implementar uma **lista de dicionários** (uma lista contento dicionários dentro) `[EXIGÊNCIA DE CÓDIGO 7 de 8]`;
8. Deve-se inserir comentários **relevantes** no código `[EXIGÊNCIA DE CÓDIGO 8 de 8]`;
9. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome `[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6]`;
10. Deve-se apresentar na saída de console um cadastro de 3 livros (sendo 2 deles no mesmo autor) `[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6]`;
11. Deve-se apresentar na saída de console uma consulta de todos os livros `[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6]`;
12. Deve-se apresentar na saída de console uma consulta por código de um dos livros `[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6]`;
13. Deve-se apresentar na saída de console uma consulta por setor em que 2 livros sejam do mesmo autor `[EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6]`;
14. Deve-se apresentar na saída de console uma remoção de um dos livros seguida de uma consulta de todos os livros `[EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6]`;

