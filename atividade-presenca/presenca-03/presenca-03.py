<<<<<<< HEAD
class Pilha:
  def __init__(self):
      self.element = list()

  def inserir(self,name):
      self.element.append(name)
      print(f'Inserindo o elemento {name}: ' + ' '.join(self.element))
=======
pilha = list()
print("Pilha: ", pilha)

def inserir(nome):
    pilha.append(nome)
    print(f'\nInserindo o elemento {nome}: ' + ' '.join(pilha))
>>>>>>> 9ad93867ac890597e55c4373d775a1c8144f5e43

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
