arq2 = open('files/arquivo1.txt', 'a', encoding='utf-8')

arq2.write(' Acrescentando conteúdo')

arq2.close()

arq2 = open('files/arquivo1.txt', 'r', encoding='utf-8')

print(arq2.read())


