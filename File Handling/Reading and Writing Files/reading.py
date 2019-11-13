arq1 = open('files/arquivo1.txt', 'r', encoding='utf-8')

print(arq1.read())

print('Nº:', arq1.tell())

print(arq1.seek(0, 0))

print(arq1.read(6))

print(arq1.read())
