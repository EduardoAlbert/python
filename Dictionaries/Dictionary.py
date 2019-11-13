"""filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

print(filme.values())
print(filme.keys())
print(filme.items())

for value in filme.values():
    print(value)

for key, value in filme.items():
    print(f'O {key} é {value}')
"""

"""locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]

print(locadora[2]['titulo'])
"""

"""pessoas = {'nome': 'Eduardo', 'sexo': 'M', 'idade': 18}

print(f'{pessoas["nome"]}')
"""

"""Brasil = list()

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

Brasil.append(estado1)
Brasil.append(estado2)

print(Brasil[1]['sigla'])
"""

estado = dict()
brasil = list()

for i in range(0, 3):

    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla de Estado: '))
    brasil.append(estado.copy())

print(brasil)

for estados in brasil:
    for key, value in estados.items():
        print(f'O campo {key} tem valor {value}.')
    print()
