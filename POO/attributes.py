class Funcionarios:
  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario

  def listFunc(self):
    print(f'O nome do funcionario é {self.nome} e o salário é R${str(self.salario)}')

Func1 = Funcionarios('Obama', 20000)

Func1.listFunc()

print(hasattr(Func1, 'nome'))

print(hasattr(Func1, 'salario'))

setattr(Func1, 'salario', 4500)
Func1.listFunc()

print(getattr(Func1, 'salario'))

delattr(Func1, 'salario')
print(hasattr(Func1, 'salario'))

