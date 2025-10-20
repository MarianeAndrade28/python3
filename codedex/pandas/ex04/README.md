# Masmorras e Dragões I

### Acessando colunas específicas.
Às vezes, não precisamos do DataFrame inteiro, pois queremos focar apenas em uma coluna (ou algumas).

Vejamos o exemplo usando o nosso já conhecido DataFrame `movies`:

<div align="center">
  <img width="1000" alt="image" src="https://github.com/user-attachments/assets/d62f7dde-5b39-489e-9c48-29ed0f3fac5f" />
</div>


Caso quiséssemos apenas o **genre** coluna, poderíamos acessá-lo usando:

```python
movies['genre']
# ou
movies.genre
```

O estilo de colchetes `(df['column_name']` é um pouco mais comum, pois é **mais versátil**. Por exemplo, se o nome da coluna conter um espaço, a notação de ponto (`df.colunm name`) falhará. A maneira correta de acessá-la seria usando os colchetes: `df['nome da coluna']`.

### Série.
Quando selecionamos uma única coluna, na verdade obtemos uma **Série Pandas** (e não um DataFrame completo). Se um DataFrame é como uma tabela, a Série é como uma **única coluna** dessa tabela. Ela ainda é poderosa, apenas mais unidimensional.

Podemos verificar isso usando a função `type()`:

```python
type(movies)            # Retorna: <class 'pandas.core.frame.DataFrame'>
type(movies['genre'])   # Retorna: <class 'pandas.core.series.Series'>
```

### Acessando várias Colunas.
Podemos acessar várias colunas usando uma lista Python de nomes de colunas. Por exemplo, a seguinte linha de  código retornaria as colunas `genre` e `studio`:

```python
only_genre_and_studio_df = movies[['genre', 'studio']]
```

### Acessando todas as colunas, exceto uma, com .drop().
Às vezes queremos todas as colunas, exceto uma. É aí que o método `.drop()` é útil:
```python
removed_title_df = movies.drop("title", axis = 1)
```

A linha de código acima cria um novo DataFrame denominado `removied_tittle_df` que contém todas as colunas de movies, exceto a coluna `title`.
O argumento `axis = 1` é fundamental, pois ele instrui o Pandas a remover uma coluna (o eixo 1) em vez de uma linha (o eixo 0, que é o padrão).

