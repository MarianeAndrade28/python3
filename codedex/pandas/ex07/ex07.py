import pandas as pd

data = {
    'app_name': ['Instagram', 'TikTok', 'Spotify', 'Waze', 'Duolingo', 'VSCO', 'Netflix', 'Twitter', 'Pinterest', 'Shazam'],
    'category': ['Social', 'Social', 'Music', 'Navigation', 'Education', 'Photo', 'Video', 'Social', 'Social', 'Music'],
    'downloads_millions': [1000, 2000, 400, 150, 300, 100, 700, 500, 600, 90],
    'price': [0.0, 0.0, 9.99, 0.0, 0.0, 0.0, 45.99, 0.0, 0.0, 0.0],
    'rating': [4.5, 4.2, 4.7, 4.4, 4.6, 4.0, 3.9, 4.3, 4.1, 4.8]
}
apps = pd.DataFrame(data)

# INSTRUÇÕES DO EXERCÍCIO:

# Adicionar uma coluna chamada 'downloaded'
apps['downloaded'] = [False, True, True, False, True, False, False, True, False, True]

# Classificar por 'rating' (Melhores no topo -> decrescente)
apps = apps.sort_values(by='rating', ascending=False)

# Alterar o nome da coluna 'app_name' para 'name'
apps = apps.rename(columns={'app_name': 'name'})

# Exibir o resultado final
print("--- Resultado Final ---")
print(apps)
