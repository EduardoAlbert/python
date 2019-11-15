class Book():
  def __init__(self, title, author, pages):
    print('Livro Criado')
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self):
    return f"Título: {self.title}, autor: {self.author}, pages: {self.pages}"

  def __len__(self):
    return self.pages

  def len(self):
    return print(f'Páginas do livro com método comum: {self.pages}')

livro1 = Book('Os Lusíadas', 'Luis de Camões', 8816)

# SPECIAL METHODS

print(livro1)

print(str(livro1))

print(len(livro1))

livro1.len()

del livro1.pages # livro1.__delattr__('pages')

print(hasattr(livro1, 'pages'))