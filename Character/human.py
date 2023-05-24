class Human:

  def __init__(self,name):
    self.name = name
    self.health = 100
    self.coins = 1000
    self.inventory = []

  def Purchase(self, item):
    if item.price <= self.coins:
      self.inventory.append(item)
      self.coins -= item.price 
      '''
      the cost should be paid to the shop
      i.e. the amount shoud be reflected in the shop a/c but currently there is no provision for that.
      '''
 
    else:
      print('Not eough credits')

  def Attack(self, obj ):
    if len(self.inventory) != 0:
      #find weapon in inventory and then use it
      for i in self.inventory:
        if i.type == 'Weapon' :
          
          #the following operation should not be permitted
          #obj.health -= i.damage , instead use the func TakeDamage
          #variables are yet to be declared as private
          obj.TakeDamage(i.damageCaused) #cause damage using weapon
          if obj.health == 0:
            print(obj.type + ' was killed')
          return #return from Attack func once weapon is used
      print('No weapon in inventory, cannot attack.')
    else:
      print('No weapon in inventory, cannot attack.')

  def TakeDamage(self, val):
    self.health -= val
    if self.health == 0:
      print( self.name + " was slaid.")