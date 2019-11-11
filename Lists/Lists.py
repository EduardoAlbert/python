valores = list()
for times in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')
