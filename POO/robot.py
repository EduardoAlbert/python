class Robot():
  
  # CONSTRUCTOR / ATRIBUTTES
  def __init__(self, name='R2D2'):
    self.name = name
    self.weight = 90
    print(f'New Robot Declared: {self.name}')

  # METHODS
  def say_hi(self, owner='My master'):
    print(f'Hi {owner}, my name is {self.name}')

  def walk(self):
    print(f'{self.name} is walking')

  def turn_right(self):
    print(f'{self.name} is turning right')

  def turn_left(self):
    print(f'{self.name} is turning left')


R2d2 = Robot()

R2d2.say_hi(owner='Albert')
R2d2.walk()
R2d2.turn_right()
R2d2.walk()
R2d2.turn_left()

print(f'My weight is {R2d2.weight}')
