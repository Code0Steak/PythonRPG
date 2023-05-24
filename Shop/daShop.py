from Tools.tools import Knife, Axe

class Shop:
  def __init__(self, name):
    self.name = name
    self.stock = [1,1,0,1] #There are 3 items Knife, Axe, Sword. There quantities avlb in the shop currently are mentioned.
    #the last item(with index 3) in stock is Medkit.