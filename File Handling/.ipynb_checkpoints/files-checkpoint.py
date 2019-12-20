texto = open('arquivodetexto', 'r', encoding='utf-8')
print(texto.read())
texto.close()

texto = open('arquivodetexto', 'w', encoding='utf-8')
texto.write('Eduardo Albert')
texto.close()

texto = open('arquivodetexto', 'r', encoding='utf-8')
print(texto.read())
