"""def title(text):
    print('-'*30)
    print(f'{text:^30}')
    print('-'*30)


title('Curso em vídeo')
"""

"""
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# Main Program
soma(4, 5)
soma(b=4, a=5)
"""

"""
def contador(*num):
    tot = len(num)
    print(f'Recebi os valores {num} e são ao todo {tot} números')


contador(2, 3)
contador(1, 2, 3)
"""

"""
def dobra(lista):
    for pos in range(0, len(lista)):
        lista[pos] *= 2


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
"""


def soma(*valores):
    print(sum(valores))


soma(3, 4, 6, 2, 1)
