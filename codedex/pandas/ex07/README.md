# 📖 Revisão

### Parabéns!
Você chegou ao final do primeiro capítulo sobre Pandas e DataFrames! Belo trabalho!

Vamos recapitular as principais conclusões deste capítulo:
DataFrames armazenam dados em linhas e colunas. Eles podem ser criados a partir de dicionários, listas ou importados diretamente de arquivos.

<br>

**Algumas explorações preliminares de dados:**
* `.head()` mostra as primeiras linhas do DataFrame;
* `.tail()` mostra as últimas linhas do DataFrame;
* `.info()` exibe nomes de colunas, tipos de dados, etc;
* `.describe()` resume estatísticas para colunas numéricas;
* Selecione colunas específicas de um DataFrame usando colchetes `[]`;
* Filtre linhas de DataFrames usando expressões booleanas como `>`, `<`, ou `==`. Encadeia múltiplas expressões booleanas usando **AND** (`&`) e **OU** (`|`);
* Podemos **classificar**, **renomear** e **adicionar** novas colunas a um **DataFrame**.

**Vamos juntar tudo isso com um exercício final.**

<br>

---
# 📝 Exercício 07

**Instruções:**
É hora de deixar nossa criatividade brilhar! Crie um DataFrame sobre um tópico de sua escolha, ele deve ter pelo menos 10 linhas e 5 colunas. Uma vez criado, execute as seguintes operações:
* Adicionar uma nova coluna;
* Classifique o DataFrame por uma coluna específica;
* Filtre linhas com base em uma ou mais condições.
<br>

Se você está tendo problemas para pensar em tópicos, aqui estão algumas ideias para começar:
* **Estatísticas** sobre seu time esportivo favorito;
* **Dados** sobre seus filmes, livros, videogames ou músicas favoritos;
* **Informações** sobre seus amigos e familiares.

**Nota:** Se precisar de ajuda para criar seu conjunto de dados, sinta-se à vontade para usar **ChatGPT** ou outra ferramenta de IA para começar (ou para gerar um ponto de partida). Descobrimos que o seguinte prompt ajudou a criar um bom DataFrame inicial:
```Dê-me um código para criar um DataFrame sobre [seu tópico] com mais de 10 linhas e mais de 5 colunas. Algumas das colunas devem ser sobre [X, Y, Z].```

**💡 Dica:**
* Usando o prompt acima, conseguimos criar um enorme **DataFrame** de Pokémon fictícios!
* Criamos então uma nova coluna que define o `power_score` com base no `attack`, `sp_atk` e `speed` de cada Pokémon;
* Em seguida, classificamos o DataFrame por este novo `power_score`;
* Por fim, filtramos para mostrar apenas os Pokémon lendários. Descobrimos que nosso Pokémon lendário mais forte foi nomeado Pokemon_70;

**Lembre-se de importar `pandas` como `pd` no início do seu notebook!**
