arq2 = open('files/arquivo1.txt', 'w', encoding='utf-8')

arq2.write('Testando gravação de arquivos em Python')

arq2.close()

arq2 = open('files/arquivo1.txt', 'r', encoding='utf-8')

print(arq2.read())
