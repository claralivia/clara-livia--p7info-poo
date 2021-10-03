class Pilha:
  def __init__(self):
      self.element = list()

  def inserir(self,name):
      self.element.append(name)
      print(f'Inserindo o elemento {name}: ' + ' '.join(self.element))

  def remover(self):
      self.element.pop()
      print(f'Removendo o último elemento: ' + ' '.join(self.element))

  def exibir(self):
      print('Pilha: ' + ' '.join(self.element))

fila = Pilha()
fila.inserir('apple')
fila.inserir('grape')
fila.inserir('lemon')

fila.remover()

fila.exibir()
