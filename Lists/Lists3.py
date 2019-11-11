'''pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][1])'''

# ------------
'''teste = list()
teste.append('Eduardo')
teste.append(18)

galera = list()
galera.append(teste[:])

teste[0] = 'Albert'
teste[1] = 19

galera.append(teste[:])
print(galera)'''

# ----------

'''character = [['Lee Sin', 35], ['Yasuo', 73], ['Magaiver', 27], ['Ana', 22]]

for per in character:
    print(f'{per[0]} tem {per[1]} de idade!')'''

# ----------

galera = list()
dados = list()
totMaior = totMenor = 0

for cont in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totMaior += 1

    else:
        print(f'{p[0]} é menor de idade.')
        totMenor += 1

print(f'Temos {totMaior} maiores e {totMenor} menores de idade.')


