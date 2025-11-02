import pandas as pd

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

characters = pd.DataFrame(characters_data)

# Exercício 05:

high_level = characters[characters["level"] > 5]

halfling_bards = characters[
    (characters["race"] == "Halfling") &
    (characters["class"] == "Bard")
]

magic_users = characters[
    (characters["class"] == "Wizard") | 
    (characters["class"] == "Sorcerer") | 
    (characters["class"] == "Warlock")
]

print(high_level)
print('-'*60)
print(halfling_bards)
print('-'*60)
print(magic_users)
