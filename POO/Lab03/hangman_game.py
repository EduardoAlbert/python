# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman():

  # Método Construtor
  def __init__(self, word):
    self.word = word
    self.hits = []
    self.wrong = []

  # Método para adivinhar a letra
  def guess(self, letter):
    if (letter in self.word and letter not in self.hits):
      [self.hits.append(l) for l in self.word if l == letter]
    elif (letter not in self.word and letter not in self.wrong):
      self.wrong.append(letter)

  # Método para verificar se o jogo terminou
  def hangman_over(self):
    return (len(self.wrong) == 6) or self.hangman_won()

  # Método para verificar se o jogador venceu
  def hangman_won(self):
    if (len(self.hits) == len(self.word)):
      return True

  # Método para não mostrar a letra no board
  def hide_word(self):
    for l in self.word:
      print(l if l in self.hits else '_', end='')

  # Método para checar o status do game e imprimir o board na tela
  def print_game_status(self):
    print(board[len(self.wrong)])

    print('\nPalavra: ', end='')
    self.hide_word()

    print('\n\nLetras erradas: ', end='')
    for l in self.wrong: 
      print(l, end=' ')

    display = []
    print('\n\nLetras corretas: ', end='')
    for l in self.hits:
      if (l not in display):
        print(l, end=' ')
        display.append(l)


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
  with open("palavras.txt", 'rt') as f:
    bank = f.readlines()
  return bank[random.randint(0, len(bank)) - 1].strip()


# Função Main - Execução do Programa
def main():

  # Objeto
  game = Hangman(rand_word())
  
  # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
  while not game.hangman_over():
    game.print_game_status()
    game.guess(str(input('\n\nDigite uma letra: ')))

  # Verifica o status do jogo
  game.print_game_status()

  # De acordo com o status, imprime mensagem na tela para o usuário
  if game.hangman_won():
    print('\n\nParabéns! Você venceu!!')
  else:
    print('\n\nGame over! Você perdeu.')
    print(f'A palavra era {game.word}')
  
  print('\nFoi bom jogar com você! Agora vá estudar')

# Executa o programa
if __name__ == "__main__":
  main()