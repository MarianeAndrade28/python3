# 📝 Questão 3
Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
A copiadora opera da seguinte maneira:
* Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
* Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
* Serviço de Impressão Preto e Branco (IBO) o custo por página é de quarenta centavos; 
* Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 
<br>

* Se número de páginas for **menor** que 20 retornar o número de página sem desconto;
* Se número de páginas for **igual ou maior** que 20 e **menor** que 200 retornar o número de páginas com o desconto é de 15%;
* Se número de páginas for **igual ou maior** que 200 e **menor** que 2000 retornar o número de páginas com o desconto é de 20%;
* Se número de páginas for **igual ou maior** que 2000 e **menor** que 20000 retornar o número de páginas com o desconto é de 25%;
* Se número de páginas for **maior ou igual** à 20000 não é aceito pedidos nessa quantidade de páginas;
<br>

* Para o **adicional** de encadernação simples (1) é cobrado um valor **extra** de 15 reais;
* Para o **adicional** de encadernação de capa dura (2) é cobrado um valor **extra** de 40 reais;
* Para o **adicional** de não querer mais nada (0) é cobrado um valor **extra** de 0 reais;
<br>

**O valor final da conta é calculado da seguinte maneira:**
```python
total = serviço * num_pagina + extra
```
<br>

**Elabore um programa em Python que:**
1. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome `[EXIGÊNCIA DE CÓDIGO 1 de 7]`;
<br>

2. Deve-se implementar a função `escolha_servico()` em que: `[EXIGÊNCIA DE CÓDIGO 2 de 7]`;
   * Pergunta o **serviço** desejado;
   * Retorna o **valor do serviço** com base na escolha do usuário;
   * Repete a pergunta do item B.a se digitar **serviço** se digitar uma opção diferente de: dig/ico/ibo/fot;
<br>

3. Deve-se implementar a função `num_pagina()` em que: `[EXIGÊNCIA DE CÓDIGO 3 de 7]`;
   * Pergunta o **número de páginas**;
   * Retorna o **número de páginas** com desconto seguindo a regra do enunciado;
   * Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico)
<br>

4. Deve-se implementar a função `servico_extra()` em que: `[EXIGÊNCIA DE CÓDIGO 4 de 7]`;
   * Pergunta pelo serviço **adicional**;
   * Retornar uma das **opções** de **adicional**; 
   * Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;
<br>

5. Deve-se implementar o total a pagar na parte do main conforme o enunciado `[EXIGÊNCIA DE CÓDIGO 5 de 7]`;
6. Deve-se implementar **try/except** `[EXIGÊNCIA DE CÓDIGO 6 de 7]`;
7. Deve-se inserir comentários relevantes no código `[EXIGÊNCIA DE CÓDIGO 7 de 7]`;
8. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome `[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4]`;
9. Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de serviço `[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]`;
10. Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou no número de páginas `[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4]`;
11. Deve-se apresentar na saída de console um pedido com opção de serviço, número de páginas e serviço extra válidos `[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4]`;

