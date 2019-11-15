class Dog():

  def __init__(self, breed):
    self.breed = breed
    print('Constructor called to create a object of this class')
  
Rex = Dog(breed='Labrador')
Golias = Dog(breed='Huskie')

print(Rex.breed)
print(Golias.breed)
