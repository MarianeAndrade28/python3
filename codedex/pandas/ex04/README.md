# Masmorras e Dragões I

### Acessando colunas específicas.
Às vezes, não precisamos do DataFrame inteiro, quando queremos ampliar apenas uma coluna (ou algumas).

Vejamos o exemplo usando nosso movies DataFrame:

<div align="center">
  <img width="1000" alt="image" src="https://github.com/user-attachments/assets/d62f7dde-5b39-489e-9c48-29ed0f3fac5f" />
</div>

Caso quiséssemos apenas o genre coluna, poderíamos acessá-la usando `movies['genre']` ou movies.genre.

O estilo do suporte `(df['column_name']` é um pouco mais comum, pois é mais versátil. Por exemplo, df.colunm name é inútil pois o nome da coluna contém um espaço. A maneira correta seria algo como: `df['column_name']`.

### Série.
Quando selecionamos uma única coluna, na verdade obtemos uma série Pandas (não um DataFrame completo). Se um DataFrame for como uma tabela, a Série é como uma única coluna dessa tabela. Ainda é poderoso, apenas mais estreito.

Vamos verificar usando `type()`:

```python
type(movies)            # Prints pandas.core.frame.DataFrame
type(movies['genre'])   # Prints pandas.core.series.Series
```

### Acessando várias Colunas.
