text = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
text = text + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
text += "E claro, em Big Data."

import os

file = open(os.path.join('cientista.txt'), 'w', encoding='utf-8')

for word in text.split():
  file.write(f'{word} ')

file.close()