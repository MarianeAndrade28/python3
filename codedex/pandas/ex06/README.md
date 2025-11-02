# 📊 Classificação, Renomeação e Adição de Colunas

### Manipulações Avançadas de Dados
Agora que exploramos e filtramos nossos dados, vamos subir de nível. Iremos aprender a classificar, renomear colunas e até a adicionar novas.

#### 1 - Classificação por Colunas com `.sort_values()`
Vamos ver qual filme rendeu mais dinheiro? Para isso, podemos classificar um DataFrame por uma coluna específica usando `.sort_values()`:

```python
box_office_sorted = movies.sort_values(by='box_office', ascending=False)
```
O novo `box_office_sorted` DataFrame terá linhas ordenadas pelo valor de sua coluna `box_office` do maior para o menor.

<div align="center">
  <img width="1000" alt="image" src="https://github.com/user-attachments/assets/fd307051-f9d4-493b-a156-09e7f43859ee" />
</div>

Para classificar de baixo para cima (ordem crescente), basta utilizar `ascending = True`.

#### 2 - Renomear Colunas com `.rename()`
Digamos que queremos renomear a coluna `'budget'` para `'budget_usd'`. Podemos fazer isso usando `.rename()`:

```python
movies = movies.rename(columns={'budget': 'budget_usd'})
```
<div align="center">
  <img width="1000" alt="image" src="https://github.com/user-attachments/assets/4dbbcfd0-2a0e-4200-aae5-c8583f129fbc" />
</div>
<br>
Observe que utilizamos `movies =` . Isso acontece pois, o método `.rename()` não modifica o DataFrame original por padrão, a menos que atribuamos o resultado de volta a `movies` (ou usemos o parâmetro `inplace=True`).

Se quiséssemos renomear várias colunas de uma só vez, poderíamos ter passado pares adicionais de chave:valor para o dicionário `columns`.

### Adicionando colunas
Podemos adicionar novas colunas atribuindo uma lista ou um cálculo ao nome de uma coluna. Vejamos como adicionar a coluna `'lead_actor'`.

```pythom
movies['lead_actor'] = ['Keanu Reeves', 'Leonardo DiCaprio', 'Song Kang-ho', 'Matthew Broderick', 'Michelle Yeoh']
```

<div align="center">
  <img width="1000" alt="image" src="https://github.com/user-attachments/assets/33c56573-d059-4246-9640-46fa7bdaf582" />
</div>
<br>

Também podemos adicionar novas colunas com base em dados existentes! Por exemplo:
```python
movies['budget (millions)'] = movies['budget'] / 1000000
```

<div align="center">
  <img width="1500" alt="image" src="https://github.com/user-attachments/assets/c60c10d9-88ac-4dd8-b718-0ccab8f820e0" />
</div>
<br>

**Agora temos números orçamentais num formato mais amigável: milhões!**

---
# 📝 Exercício 06

### Instruções:
Carregamos dados sobre aplicativos populares em um DataFrame chamado `apps`.

**Edite o DataFrame das seguintes maneiras:**
* Comece adicionando uma coluna chamada `downloaded` que contém `True` ou `False` dependendo se você baixou o aplicativo no seu telefone;
* Classifique os aplicativos por `rating`, de modo que os aplicativos com melhor classificação estejam no topo do DataFrame;
* Altere o nome da coluna `app_name` para `name`.

###  💡 Dica:
* Para criar uma nova coluna, defina `apps['downloaded']` igual a uma **lista de 10 itens**;
* Usar `apps.sort_values()` para classificar o DataFrame por `rating`. Certifique-se de incluir `ascending = False`;
* Para renomear uma coluna, use `apps.rename()` e passe o dicionário `columns={'app_name':'name'}`.


