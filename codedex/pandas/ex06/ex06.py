import pandas as pd
import numpy as np

# Esqueleto do DataFrame 'apps' (dados do Codédex)
app_data = {
  'app_name': [
    'YouTube', 'TikTok', 'Instagram', 'Spotify', 'Duolingo', 
    'Twitter', 'Headspace', 'Discord', 'Depop'
  ],
  'category': [
    'Video', 'Social Media', 'Social Media', 'Music', 'Education',
    'Social Media', 'Health', 'Communication', 'Shopping'
  ],
  'rating': [
    4.7, 4.6, 4.5, 4.6, 4.7,
    4.3, None, 4.7, 4.4
  ],
  'downloads_millions': [
    5000, 3000, 3500, 2000, None,
    1500, 500, 600, 200
  ]
}

# Criação do DataFrame
apps = pd.DataFrame(app_data)

# Imprimir o DataFrame original para referência
print("--- 1. DataFrame Original (apps) ---")
print(apps)
print("-" * 50)

# Adicionar uma coluna chamada 'downloaded'
# (Dica: lista de 9 itens para corresponder às 9 linhas, True ou False)
apps['downloaded'] = [True, True, True, True, False, False, False, True, False]

print("--- 2. Coluna 'downloaded' Adicionada ---")
print(apps)
print("-" * 50)


# Classificar os aplicativos por rating, de modo que os aplicativos com melhor classificação estejam no topo
# (Dica: use .sort_values() com ascending=False)
apps_sorted = apps.sort_values(by='rating', ascending=False)

print("--- 3. Classificação por 'rating' (Melhor no topo) ---")
print(apps_sorted)
print("-" * 50)


# Altera o nome da coluna app_name para name
# (Dica: use .rename() e passe o dicionário columns={'app_name':'name'})
# Usar inplace=True para modificar o DataFrame 'apps' diretamente.
apps.rename(columns={'app_name': 'name'}, inplace=True)

print("--- 4. Coluna 'app_name' Renomeada para 'name' ---")
print(apps)
print("-" * 50)
