from Tools.tools import Tool, weaponDict, healPrice

from prettytable import PrettyTable

class Human:

  def __init__(self,name):
    self.name = name
    self.health = 100
    self.coins = 1000
    self.inventory = []


  def PurchaseFromShop(self,shop):
    print()
    print(f'Current Coin balance: {self.coins} units')
    #menu options for shop
    table = PrettyTable()
    
    table.field_names = ['Item','Price','Selection Key']
    table.add_rows([
      [f'{shop.items[0]}',f'{weaponDict[0][1]}','0'],
      [f'{shop.items[1]}',f'{weaponDict[1][1]}','1'],
      [f'{shop.items[2]}',f'{weaponDict[2][1]}','2'],
      [f'{shop.items[3]}',f'{healPrice}','3']
    ])

    table.border = True 
    table.header_style = "upper"
    table.align = "l"
    table.border = True 
    table.header_style = "upper"
    table.align = "l"
    print(table)
    id = int(input('Enter Selection Key for the Item you want to purchase: ')) #select from prompt
    #basic validation check for id
    if id < 0 or id > 3:
      print('Invalid selection')
      print()
      return 
    

  #if you are not purchasing 'Heal'
    if id != 3:


    #check if item in shop's stock
      if shop.stock[id] == 0:
        print(f'{weaponDict[id][0]} is unavailable, please opt for restock')
        print()
        return 

      #check if payable
      if self.coins < weaponDict[id][1]:
        print(f'Unsufficient balance to purchase {weaponDict[id][0]}')
        print()
        return

      #check if item already present
      for obj in self.inventory:
        if obj.name == weaponDict[id][0]:
          print(f"{obj.name} already present in Inventory")
          print()
          return

      #item is available and also sufficient balance, hence
      shop.stock[id] -= 1 #reduce frm stock
      self.coins -= weaponDict[id][1] #deduct
      #add new Tool() to inventory. 
      self.inventory.append(Tool(id,weaponDict[id][0],'Weapon'))
      print()
      print(f'Item {self.inventory[len(self.inventory) - 1].name} purchased. Current Coin balance : {self.coins} units')
      print()
    # if shop.stock[id] == 0:
    #   print('Item unavailable in stock')
    #   return
    else:
      if shop.stock[id] == 0:
        print('Heal item unavailable. Please opt for restocking')
        print()
        return 

      if self.coins < healPrice:
        print('Unsufficient coins to purchase healing/medkit')
        print()
        return
      
      #check if Heal already present
      for obj in self.inventory:
        if obj.name == weaponDict[id][0]:
          print('Heal item already present')
          print()
          return

      self.inventory.append(Tool(id, 'Medkit', 'Heal'))
      print()
      self.coins -= weaponDict[id][1]#deduct
      print(f'Item {self.inventory[len(self.inventory) - 1].name} purchased. Current Coin balance : {self.coins} units')
      print()


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
        print('No Weapons available in inventory. Better purchase them from the Shop 🏬')
        return 
      
      print(f'(Instruction for {self.name}:) Pick a weapon to Fight')
      
      table = PrettyTable()
      table.field_names = [i for i in range(len(weapons))]

      table.add_row([self.inventory[i].name for i in weapons ])
      print(table)
      
      id = int(input('Select weapon by key from above table: '))
      if id < 0 or id > len(self.inventory):
        print('Invalid selection.')
        print()
        return 
      if self.inventory[id].type != 'Weapon':
        print('Not a weapon. Please select a weapon from the given choices')
        print()
        return 
      
      #finally you have the id of the weapon chosen 
      #attack using the weapon
      obj.TakeDamage(self.inventory[id].damage)
      print(f'{self.name} vs {obj.name}. You dealt {self.inventory[id].damage} damage.')
      self.inventory[id].durability -= 1 #reduce durability because of 1 hit.
      if self.inventory[id].durability <= 0:
        print(f'Uh, oh. Your {self.inventory[id].name} is no longer usable!! It served you well 🙏')
        del self.inventory[id] #delete item if destroyed.

      if obj.getHealth() == 0:
        if obj.type == 'Zombie':
          self.coins += 50 #earn 50 by killing zombie 
          print('You earned 50 coins by slaying the Zombie')
        elif obj.type == 'Vampire':
          self.coins += 300
          print('You earned 300 coins by slaying the Vampire')
      
    else:
      print('No weapon in inventory, cannot attack.')
   
  def TakeDamage(self, val):
    self.health -= val
    if self.health == 0:
      print( self.name + " was slaid")

  def Restock(self, shop):
    print('Select item to restock:-')
    for i in range(3):
      print(f'{i}: {weaponDict[i][0]}, price: {weaponDict[i][1]}')
    
    print(f'{3}: Heal, price: 100')

    id = int(input('Restock selection: '))
    if id < 0 or id > 3:
      print('Invalid selection')
      return 
    
    shop.stock[id] += 1 
    print('The item has been restocked.')
  
  def healSelf():
    
    ind = 0
    for ob in self.inventory:
      if ob.type == 'Heal':
        self.health += ob.healVal
        if self.health > 100:
          self.health = 100
        del self.inventory[ind]
        return
      ind += 1
    
    print('No Heal item in Inventory')
        