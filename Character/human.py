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

      #check if item already present
      for obj in self.inventory:
        if obj.name == weaponDict[id][0]:
          print("{} already present in Inventory")
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
      
      #check if Heal already present
      for obj in self.inventory:
        if obj.name == weaponDict[id][0]:
          print('Heal item already present')
          return

      self.inventory.append(Tool(id, 'Medkit', 'Heal'))


  def Attack(self, obj ):
    if len(self.inventory) != 0:
      #make a list of indices of weapons present in inventory 
      weapons = []
      i = 0
      for ob in self.inventory:
        if ob.type == 'Weapon':
          weapons.append(i) 
        i += 1
      
      if len(weapons) == 0:
        print('No Weapons available in inventory. Better purchase them from Shop.')
        return 
      
      print('Pick a weapon')
      i = 0
      for ind in weapons:
        print(ind,f': {self.inventory[ind].name}')
      
      id = int(input('Choice: '))
      if id < 0 or id > len(self.inventory):
        print('Invalid choice.')
        return 
      if self.inventory[id].type != 'Weapon':
        print('Not a weapon. Please select a weapon from the given choices')
        return 
      
      #finally you have the id of the weapon chosen 
      #attack using the weapon
      obj.TakeDamage(self.inventory[id].damage)
      self.inventory[id].durability -= 1 #reduce durability because of 1 hit.
      
    else:
      print('No weapon in inventory, cannot attack.')
   
  def TakeDamage(self, val):
    self.health -= val
    if self.health == 0:
      print( self.name + " was slaid.")