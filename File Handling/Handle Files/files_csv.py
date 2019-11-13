import csv

# writing

""" with open('files/numeros.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerow(('primeira', 'segunda', 'terceira'))
  writer.writerow((55, 93, 76))
  writer.writerow((62, 14, 86)) """

# reading

""" with open('files/numeros.csv', 'r') as file:
  reader = csv.reader(file)
  for x in reader:
    print(x) """

# reading in list

with open('files/numeros.csv', 'r') as file:
  reader = csv.reader(file)
  data = list(reader)

print(data)

for linha in data[1:]:
  print(linha)