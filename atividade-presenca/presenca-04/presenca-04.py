# -*- coding: utf-8 -*-
class Fila:
  def __init__(self):
      self.element = list()
  def inserir(self,name):
      self.element.append(name)
      print(f'Inserindo o elemento {name}: ' + ' '.join(self.element))
  def remover(self):
      self.element.pop(0)
      print(f'Removendo o primeiro elemento: ' + ' '.join(self.element))
  def exibir(self):
      print('Fila: ' + ' '.join(self.element))

fila = Fila()
fila.inserir('apple')
fila.inserir('grape')
fila.inserir('lemon')

fila.remover()

fila.exibir()
