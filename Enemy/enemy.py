class Enemy:

  def __init__(self, name):
    self.name = name
    self.health = 100
    #enemies can have weapons in their inventory as well. but let's keep it simple
    self.dropCoins = 0  #the dropCoins indicates the coins the enemy will drop once slayed.

  def Attack(self, obj):
    pass


  def TakeDamage(self, val):
    self.health -= val
    if self.health == 0:
      print(self.name + ' was slayed.')
  
  def getHealth(self):
    return self.health
  
  def getDropCoins(self):
    return self.dropCoins
  

class Zombie(Enemy):

  def __init__(self,name):
    super().__init__(name)
    self.type = 'Zombie'
    self.health = 250
    self.dropCoins = 50

  def Attack(self, obj):
    obj.TakeDamage(30)  #Zombie attacks lead to -30 health
  

class Vampire(Enemy):

  def __init__(self, name):
    super().__init__(name)
    self.type = 'Vampire'
    self.health = 950
    self.dropCoins = 300

  def Attack(self, obj):
    obj.TakeDamage(70)  #Vampires attacks are lethal
