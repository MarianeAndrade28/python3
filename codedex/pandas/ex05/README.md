# Masmorras e Dragões II

### Filtrando Linhas.
Já aprendemos como selecionar colunas específicas, mas e se quisermos apenas certas linhas? Aqui está o nosso movies DataFrame mais uma vez:

<div align="center">
  <img width="800" alt="image" src="https://github.com/user-attachments/assets/a303ae6b-a0dd-4e87-a83f-40520e403354"/>
</div>

Vejamos como podemos filtrar filmes com mais de 120 minutos:

```python
long_movies = movies[movies['runtime_minutes'] > 120]
```

Agora `long_movies` contém apenas os filmes extralongos.
<div align="center">
  <img width="800" alt="image" src="https://github.com/user-attachments/assets/996e75c7-b2a7-4d3f-ad0e-b85ae92d737f" />
</div>

Essa sintaxe de filtragem pode ser um pouco confusa. Por que precisamos incluir `movies` duas vezes?
Vamos decompô-lo observando a parte do código que está dentro do conjunto externo de colchetes: A linha `movies['runtime_minutes'] > 120` cria uma série de valores `True` e `False`, um para cada linha:

<div align="center">
  <img width="464" height="188" alt="image" src="https://github.com/user-attachments/assets/5157795c-22a9-40c7-b523-f18545aa84e5" />
</div>

Isso mostrará que em nosso movies DataFrame, todos os filmes, exceto o 4º filme (O Rei Leão) têm mais de 120 minutos.
Mas isso ainda não foi filtrado. Queremos remover as linhas com valor False. Para filtrar o DataFrame, usamos essa série booleana entre colchetes. Isso mantém apenas as linhas onde a condição está True.

Aqui está outra maneira de fazer essa filtragem, onde dividimos o processo em duas etapas:

```python
boolean_series = movies['runtime_minutes'] > 120
long_movies = movies[boolean_series]
```

### AND e OR
Podemos filtrar com base em várias condições usando AND e OR. Ou seja, se quisermos filtrar filmes com mais de 120 minutos AND do gênero `'Sci-Fi'`, devemos usar o seguinte código:

```python
long_movies = movies[
  (movies['runtime_minutes'] > 120) &
  (movies['genre'] == 'Sci-Fi')
]
```

É importante se certificar de envolver cada série booleana individual entre parênteses. Se quiser usar OR ao invés de AND, basta alterar `&` para `|`.
Podemos encadear quantas expressões desejarmos!

---
# 📝 Exercício 05

### Instruções:
Considere o DataFrame `characters`, que contém dados de vários heróis de **Dungeons & Dragons** (D&D). Usando técnicas de filtragem do Pandas, crie os três novos DataFrames solicitados abaixo:
1. `high_level`:
  * Deve incluir apenas os personagens cujo nível (`level`) seja estritamente maior que 5;
3. `halfling_bards`:
  * Deve incluir apenas os personagens cuja raça (`race`) seja `'Halfling'` AND a classe (`class`) seja `'Bard'`;
4. `magic_users`:
  * Deve incluir todos os personagens cuja classe (class) seja `'Wizard'` OR `'Sorcerer'` OR `'Warlock'`.

Após criar cada DataFrame, exiba-o para confirmar se a filtragem foi aplicada corretamente.

### 💡 Dica:
* Para os personagens `high_level`, sua declaração booleana deve ser `characters["level"] > 5`;
* Para os personagens `halflign_bard`, você precisará combinar duas declarações booleanas com um operador `&` (AND). A primeira deve ser `(characters["race"] == "Halfling"`;
* Para `magic_users` você precisará combiar três instruções booleanas com duas barras verticais `|` (OR). A primeira declaração deve ser `(characters["class"] == "Wizard")`.
