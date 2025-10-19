# 📱 Aplicativos Móveis

### Exploração de Dados.
O Pandas é ótimo para trabalhar com conjuntos de dados com milhares de linhas. No entanto, ao olharmos para uma tabela enorme (ou um DataFrame grande), pode ser difícil saber por onde começar.

Aqui estão quatro `pandas` métodos que podem ajudar em alguma exploração básica de dados:
`.head()`, `.tail()`, `.info()` e `.describe()`

### Exibir linhas com .head() e .tail().
Se o conjunto de dados for muito grande, imprimir tudo resultaria em excesso de informações na tela. É aqui que `.head()`e `.tail()`entram. Esses métodos exibem as **primeiras** e às **últimas 5 linhas** (por padrão) do DataFrame, respectivamente.

Imagine que tenhamos um DataFrame chamado `df`:
```python
df.head()     # Exibe as primeiras 5 linhas
df.tail()     # Exibe as últimas 5 linhas
```

Se quisermos mais de 5 linhas, podemos passar um número específico. Por exemplo, isso exibirá o primeiro 10 linhas:
```python
df.head(10)   # Exibe as primeiras 10 linhas
```

### Tipos de Dados e Valores Ausentes com .info().
O método `.info()` irá mostrar informações sobre colunas específicas. Imagine que tenhamos o seguinte DataFrame nomeado `movies`:

<div align="center">
  <img width="1000" alt="image" src="https://github.com/user-attachments/assets/3347efc3-bffa-4ebb-a726-eb5e7fb56a6b" />
</div>

Observe como temos `NaN` (não é um número) valores em algumas linhas. Isso é comum, pois conjuntos de dados do mundo real geralmente apresentam dados ausentes ou incompletos.
Se chamarmos `movies.info()`, nós obteremos à seguinte saída:

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 8 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   title            5 non-null      object
 1   release_date     5 non-null      object
 2   genre            5 non-null      object
 3   studio           5 non-null      object
 4   budget           4 non-null      float64
 5   box_office       4 non-null      float64
 6   runtime_minutes  5 non-null      int64
 7   rating           5 non-null      float64
dtypes: float64(3), int64(1), object(4)
memory usage: 312.0+ bytes
```

**Existem algumas informações notáveis neste resultado:**
* `5 entries` significa que existem 5 linhas no conjunto de dados;
* As colunas `budget` e `box_office` possuem 1 valor ausente (apenas 4  valores não nulos);
* O `Dtype` descreve o tipo de dados de cada coluna;
  * Números decimais são armazenados como `float64`, e números inteiros são armazenados como `int64`;
  * As colunas que armazenam _strings_ são representadas por `object`. Se as colunas armazenassem outros tipos de dados complexos, como dicionários, datas ou objetos definidos pelo usuário, elas também apareceriam como `object`.

Em suma, o método `.info()` pode ser usado para obter uma compreensão rápida dos tipos de dados armazenados no seu DataFrame, bem como **quantos dados estão faltando**.

### Estatísticas Resumidas com `.describe()`.
Imagine que queremos encontrar o orçamento médio dos filmes no seu DataFrame. Você pode usar o método `.describe()` para obter um resumo de estatísticas (média, mínimo, máximo, desvio padrão, etc) para cada coluna numérica:

```python
movies.describe()
```

<div align="center">
  <img width="600" alt="image" src="https://github.com/user-attachments/assets/eecf7df2-3b90-4404-8e40-81e514a1415f" />
</div>


Isso mostra que o orçamento médio dos nossos filmes é `7.3250000e+07`, ou 73.250.000. O método `.describe()` calcule apenas estatísticas resumidas para colunas numéricas, pois muitas dessas estatísticas não fariam sentido para _strings_.

No entanto, adicionar o parâmetro `include='all'` nos permite visualizar estatísticas sobre colunas não numéricas:

<div align="center">
  <img width="600" alt="image" src="https://github.com/user-attachments/assets/e0feda9f-e5f5-49ec-9ee3-5c884a719361" />
</div>

