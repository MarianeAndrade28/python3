import pandas as pd

data = {
  'personagem': ['Drácula', 'Martha', 'Mavis', 'Jonathan'],
  'espécie': ['Vampiro', 'Vampiro', 'Vampiro', 'Humano'],
  'telefone': ['939-555-0113', '939-555-0114', '939-555-0115', '939-555-0116'],
  'original': ['Adam Sandler', 'Jackie Sandler', 'Selena Gomes', 'Andy Samberg'],
  'dublador': ['Alexandre Moreno', 'Flávia Saddy', 'Fernanda Baronne', ' Mckeidy Lisita']
}

contatos = pd.DataFrame(data)

print(contatos)
