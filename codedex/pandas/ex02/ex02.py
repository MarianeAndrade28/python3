import pandas as pd

data = {
  'nome': ['Bart', 'Lisa', 'Homer', 'Marge'],
  'idade': [10, 8, 39, 36],
  'numero_telefone': ['939-555-0113', '939-555-0114', '939-555-0115', '939-555-0116'],
  'signo': ['Touro', 'Virgem', 'Touro', 'Peixes']
}

contatos = pd.DataFrame(data)

print(contatos)
