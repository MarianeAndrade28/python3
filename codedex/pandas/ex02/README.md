# 📑 Lista de Contatos

Depois de ver um exemplo de **DataFrame**, vamos agora nos aprofundar mais no assunto.

### Quadro de Dados
É o coração da biblioteca Pandas. Como uma planilha que podemos controlar com código: uma tabela composta por linhas e colunas, onde cada coluna contém um tipo específico de dados, como números, texto ou até mesmo datas.

### Importando Pandas
O primeiro passo, é importar o Pandas, que é comumente apelidado como `pd`: 

```python
import pandas
```

Com a importação concluída, podemos então iniciar a criação de `DataFrames`. Para o nosso exemplo de cidades, há algumas abordagens possíveis.

| CIDADE | PAÍS | POPULAÇÃO |
| :--- | :--- | :--- |
| Brooklyn | EUA | 2646000 |
| Seul | Coreia do Sul | 9411000 |
| Barcelona | Espanha | 1636000 |
| Cidade do México | México | 9209944 |

### Criando à partir de um Dicionário.
Esta é a forma mais popular de construir um DataFrame do zero:

```python
import pandas as pd

data = {
  'city': ['Brooklyn', 'Seoul', 'Barcelona', 'Mexico City'],
  'country': ['US', 'South Korea', 'Spain', 'Mexico'],
  'population': [2646000, 9411000, 1636000, 9209944]
}

df = pd.DataFrame(data)
```

Cada chave no `data` dicionário (`city`, `country`, `population`) torna-se uma coluna, e cada índice nas listas se tornará uma linha. Por exemplo, a primeira linha representará a cidade de Brooklyn, nos EUA, com uma população de 2,646 milhões de pessoas.

Uma vez criado o dicionário, podemos passar o dicionário para `pd.DataFrame()` para criar o DataFrame. Aqui, nós o armazenamos em uma variável chamada `df`, abreviação de DataFrame.

### Criando à partir de uma Lista de Listas.
Às vezes é mais fácil pensar em fileiras. Podemos fazer isso assim com uma lista 2D.

```python
data = [
  ['Brooklyn', 'US', 2646000],
  ['Seoul', 'South Korea', 9411000],
  ['Barcelona', 'Spain', 1636000],
  ['Mexico City', 'Mexico', 9209944]
]

df = pd.DataFrame(data, columns=['city', 'country', 'population'])
```

Aqui, cada lista interna é uma linha. Não se esqueça de nomear nossas colunas como o `columns` parâmetro!

### Importando de um Arquivo CSV.
Imagine que temos um .csv arquivo (valores separados por vírgulas) em nosso computador, e que queremos trazer para Python. Podemos carregá-lo no Pandas em uma linha com `.read_csv()`:

```python
df = pd.read_csv('my_filename.csv')
```

Substituir `my_filename.csv` com nome de arquivo. Se estiver na mesma pasta do código, tudo certo.

Vamos usar este método com mais frequência ao trabalhar com dados do mundo real.

### Bônus: Importando de outros tipos de Arquivo.
Às vezes, os dados chegam .tsv Formato (valores separados por tabulação) em vez de .csv. Para explicar isso, precisamos adicionar um ``delimiter`` parâmetro:

```python
df = pd.read_csv('my_filename.tsv', delimiter='\t')
```


Aqui, `delimiter='\t'` diz ao Python que os valores no **meu_nome do arquivo.tsv** os arquivos são separados por tabulações em vez de vírgulas.

