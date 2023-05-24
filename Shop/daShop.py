from Tools.tools import Knife, Axe

class Shop:
  def __init__(self, name):
    self.name = name
    self.stock = [[2, Knife],[1, Axe]]