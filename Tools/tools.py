class Tools:

  def __init__(self):
    self.price = 99
    self.damageCaused = 150
    #haven't thought of other params


class Gadgets(Tools):

  def __init__(self):
    pass


'''
Weapon class Inherits from Tools
Axe, Knife are weapons avlb in Shop.
'''

class Weapon(Tools):

  def __init__(self):
    super().__init__()  #to init weapon strength
    self.type = "Weapon"


class Axe(Weapon):

  def __init__(self):
    super().__init__()  #sets type param/property as weapon
    self.price = 90 #overriden


class Knife(Weapon):

  def __init__(self):
    super().__init__()  #sets type param/property as weapon
    self.price = 50  #overriden
    self.damageCaused = 100  #damage caused overriden
