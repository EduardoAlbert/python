temperaturas = [0, 22.5, 40, 100]

# MAP WITH NORMAL FUNCTIONS
""" 
def fahrenheit(T):
  return ((float(9)/5)*T + 32)

def celsius(T):
  return (float(5)/9)*(T-32)

print('Temps in fahrenheit:')

print(list(map(fahrenheit, temperaturas)))

for temp in map(fahrenheit, temperaturas):
  print(temp)

print('\nTemps in celsius:')

print(list(map(celsius, temperaturas)))

for temp in map(celsius, temperaturas):
  print(temp) """

# MAP WITH ANONYMOUS FUNCTIONS (lambda)
""" 
print(list(map(lambda x: (5.0 / 9)*(x - 32), temperaturas)))
 """
# SUM LIST'S ELEMENTS

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

print(list(map(lambda x,y: x+y, list1, list2)))

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]

print(list(map(lambda x,y,z: x+y+z, list1, list2, list3)))


