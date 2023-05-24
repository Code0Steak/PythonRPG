from Tools.tools import Tool, weaponDict, healPrice

class Human:

  def __init__(self,name):
    self.name = name
    self.health = 100
    self.coins = 1000
    self.inventory = []

  #test method this will be removed
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

  def PurchaseFromShop(self,shop):

    id = int(input('Please make a selection. 0 : Knife, 1 : Axe, 2 : Sword, 3: Medkit')) #select from prompt
    #basic validation check for id
    if id < 0 or id > 3:
      print('Invalid selection')
      return 
    

  #if you are not purchasing 'Heal'
    if id != 3:


    #check if item in shop's stock
      if shop.stock[id] == 0:
        print(f'{weaponDict[id][0]} is unavailable, please opt for restock')
        return 

      #check if payable
      if self.coins < weaponDict[id][1]:
        print(f'Unsufficient balance to purchase {weaponDict[id][0]}')
        return

      #item is available and also sufficient balance, hence
      shop.stock[id] -= 1 #reduce frm stock
      #add new Tool() to inventory. 
      self.inventory.append(Tool(id,weaponDict[id][0],'Weapon'))

    # if shop.stock[id] == 0:
    #   print('Item unavailable in stock')
    #   return
    else:
      if shop.stock[id] == 0:
        print('Heal item unavailable. Please opt for restocking')
        return 

      if self.coins < healPrice:
        print('Unsufficient coins to purchase healing/medkit')
        return
        
      self.inventory.append(Tool(id, 'Medkit', 'Heal'))


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