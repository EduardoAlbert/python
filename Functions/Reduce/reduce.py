from functools import reduce

numbers = [1, 2, 3, 5, 6]

""" 
def sum(a, b):
  x = a + b
  return x

print(reduce(sum, numbers)) """

#--------#

""" 
print(reduce(lambda x,y: x+y, numbers)) """

#--------#

""" max_find = lambda a,b: a if (a > b) else b

print(reduce(max_find, numbers)) """


