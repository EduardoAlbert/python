f = open('files/salarios.csv', 'r')

data = f.read()

rows = data.split('\n')

full_data = []

# Number of rows:

""" for row in rows:
  split_row = row.split(',')
  full_data.append(split_row)

count = 0
for row in full_data:
  count += 1 """

# Number of columns:

for row in rows:
  split_row = row.split(',')
  full_data.append(split_row)
  first_row = full_data[0]

count = 0

for column in first_row:
  count += 1

print(count)
