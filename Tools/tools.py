#There are 2 types of tools: 'Weapon', 'Heal' 

#Constants for the only 3 'Weapon' tools available
#The tuple here represents values for (name, price, damage, durability/no of hits) for each of the 'Weapon' tool/item


weaponDict = {
  0: ('Knife',50, 100, 4),
  1: ('Axe',90, 150, 10),
  2: ('Sword',200, 350, 2)
}

class Tool:

  def __init__(self, id, name, typ):
    self.id = id
    self.name = name 
    self.type = typ
    if self.type == 'Weapon':
      self.price = weaponDict[self.name][1]
      self.damage = weaponDict[self.name][2]
      self.durability = weaponDict[self.name][3]
    if self.type == 'Heal':
      self.price = 100 #price for medkit




healPrice = 100

#     #haven't thought of other params


# class Gadgets(Tools):

#   def __init__(self):
#     pass


# '''
# Weapon class Inherits from Tools
# Axe, Knife are weapons avlb in Shop.
# '''

# class Weapon(Tools):

#   def __init__(self):
#     super().__init__()  #to init weapon strength
#     self.type = "Weapon"


# class Axe(Weapon):

#   def __init__(self):
#     super().__init__()  #sets type param/property as weapon
#     self.price = 90 #overriden


# class Knife(Weapon):

#   def __init__(self):
#     super().__init__()  #sets type param/property as weapon
#     self.price = 50  #overriden
#     self.damageCaused = 100  #damage caused overriden
