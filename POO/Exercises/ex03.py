# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():

  def __init__(self, tamanho=5, interface='8.0'):
    self.tamanho = tamanho
    self.interface = interface


class MP3Player(Smartphone):

  def __init__(self, capacidade=25):
    Smartphone.__init__(self)
    self.capacidade = capacidade


Ipod = MP3Player(30)

print(Ipod.tamanho)
print(Ipod.interface)
print(Ipod.capacidade)