import pandas as pd

# Dados dos Personagens de D&D (Masmorras e Dragões).
characters_data = {
  'name': ['Thorne', 'Elira', 'Glim', 'Brug', 'Nyx', 'Kael', 'Mira', 'Drogan', 'Zara', 'Fenwick'],
  'race': ['Elf', 'Human', 'Gnome', 'Half-Orc', 'Tiefling', 'Dragonborn', 'Halfling', 'Dwarf', 'Aasimar', 'Goblin'],
  'class': ['Ranger', 'Cleric', 'Wizard', 'Barbarian', 'Rogue', 'Paladin', 'Bard', 'Fighter', 'Sorcerer', 'Warlock'],
  'level': [5, 3, 4, 2, 6, 7, 3, 5, 4, 2],
  'hp': [42, 28, 33, 25, 48, 56, 30, 44, 36, 24],
  'alignment': [
    'Chaotic Good', 'Lawful Good', 'Neutral', 'Chaotic Neutral', 'Chaotic Evil',
    'Lawful Neutral', 'Neutral Good', 'Neutral', 'Chaotic Good', 'Lawful Evil'
  ]
}

# Cria o DataFrame
characters = pd.DataFrame(characters_data)

# Seleciona a coluna 'name' e armazena em 'character_names'
# Nota: A seleção de uma única coluna retorna um objeto Series.
character_names = characters['name']

print(type(character_names))

# Seleciona as colunas 'name', 'level', e 'hp' usando colchetes duplos [[]]
basic_stats = characters[['name', 'level', 'hp']]

# Usa .drop() para remover a coluna 'alignment'.
# axis=1 indica que queremos remover uma coluna (eixo horizontal).
removed_alignment = characters.drop('alignment', axis=1)

print(basic_stats)
print(removed_alignment)
