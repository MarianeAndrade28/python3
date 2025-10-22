# Desafio 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# Os 5 primeiros; Os últimos 4 colocados; Times em ordem alfabética; Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print("-"*60)
print(f"Times do Brasileirão: {times}")
print("-"*60)

print(f"Os 5 primeiros são {times[0:5]}")
print("-"*60)

print(f"Os 4 últimos colocados são: {times[-4:]}")
print("-"*60)

print(f"Em ordem alfabética: {sorted(times)}")
print("-"*60)

print(f"O Chapecoense aparece na {times.index('Chapecoense')+1}ª posição")
