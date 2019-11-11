dict = {'nome': 'Guido van Rossum',
        'linguagem': 'Python',
        'similar': ['c','Modula-3','lisp'],
        'users': 1000000}

import json

# CREATING FILE  

""" 
with open('files/dados.json', 'w') as file:
  file.write(json.dumps(dict)) """

# READING

""" 
with open('files/dados.json', 'r', encoding='utf-8') as file:
  text = file.read()
  data = json.loads(text)

print(data)

print(data['nome']) """

# PRINTING A FILE JSON FROM INTERNET

""" 
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]

print(f"Título: {data['title']}")
print(f"URL: {data['url']}")
print(f"Duração: {data['duration']}")
print(f"Número de Visualizações: {data['stats_number_of_plays']}") """

# COPYING CONTENT FROM ONE TO ANOTHER

import os 

file_source = 'files/dados.json'
file_destiny = 'files/json_data.txt'

# Method 1
""" 
with open(file_source, 'r') as infile:
  text = infile.read()
  with open(file_destiny, 'w') as outfile:
    outfile.write(text) """

# Method 2

open(file_destiny, 'w').write(open(file_source, 'r').read())