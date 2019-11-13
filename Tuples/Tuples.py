champions = ('Yasuo', 'Lee Sin', 'Vayne', 'Ekko', 'Hecarim')

for champion in champions:
    print(f'Eu escolhi o capeão {champion}')

for posicao in range(0, len(champions)):
    print(f'Eu escolhi o campeão {champions[posicao]} na posição {posicao}')

for pos, champion in enumerate(champions):
    print(f'Eu escolhi o campeão {champion}, na posição {pos}')



