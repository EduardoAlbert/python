pares = []
for i in range(1, 11):
    num = int(input('Digite o {}º Número: '.format(i)))
    if num % 2 == 0:
        pares.append(num)

print('Números Pares: ', pares)
