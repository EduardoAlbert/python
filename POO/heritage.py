# Criando a classe Animal - Super-classe
class Animal():

  def __init__(self):
    print('Animal criado')

  def Identif(self):
    print('Animal')

  def comer(self):
    print('Comendo')
  
# Criando a classe Cachorro - Sub-classe

class Cachorro(Animal):

  def __init__(self):
    Animal.__init__(self)
    print('Objeto cachorro criado')

  def Identif(self):
    print('Cachorro')

  def latir(self):
    print('Au Au!')

rex = Cachorro()

rex.Identif()

rex.comer()

rex.latir()