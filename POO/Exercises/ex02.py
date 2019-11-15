# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():

  def __init__(self, nome, cidade, telefone, email):
    self.nome = nome
    self.cidade = cidade
    self.telefone = telefone
    self.email = email

  def __str__(self):
    return f'Nome: {self.nome}, Cidade: {self.cidade}, Telefone: {self.telefone}, E-mail: {self.email}'

  def __len__(self):
    return self.telefone

Usuario = Pessoa('Albert', 'São Paulo', 1999999999, 'albert-costa1@live.com')

print(Usuario)

print(len(Usuario))