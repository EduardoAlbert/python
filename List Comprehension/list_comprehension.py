""" 
lst = [x for x in 'python']

print(lst) """

#--#

""" 
lst = [ x**2 for x in range(0, 11) ]

print(lst)
 """

#--#

""" 
lst = [ x for x in range(1, 11) if x % 2 == 0 ]

print(lst) """

#--#

""" 
celsius = [0, 10, 20.1, 34.5]

fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius ]

print(fahrenheit) """

#--#

lst = [ x**2 for x in [x**2 for x in range(11)]]

print(lst)