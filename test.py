# from Character.human import Human
# from Shop.daShop import Shop
# import time, asyncio


# class GameVars:
#   def __init__(self):
#     self.duration = 5 #60sec Day, 60sec Night 
#     self.day = True #start with a day
#     self.nightCount = 0
#     self.gameStartTime = time.time() 
#     self.gameWon = False #to load stats accordingly





# if __name__ == '__main__':
#   print('GAME STARTS...\n\n')
#   _username = input('Type in a Username: ')
#   player = Human(_username)
#   gmv = GameVars()
#   shop = Shop('7/11')
#   print(f'\n\nCharacter {player.name} created. Some Game Variables declared...')
#   print(f'Hey, {player.name}! Welcome to the Game. The following Instructons might come in handy, please go through them and hit ENTER once done.\n')
#   print(f'1. The Goal of the game is \'Survival\'......')
#   rw = input() #the game will start after the user hits ENTER

#   def dayActivity():
#     print('Day') #todo: generate random day quotes
#     print('\'p\' - to purchase\n\'r\' - to restock\n\'h\' - to heal')

#     while gmv.day:
#       op = input('Type (activity) key and ENTER:')
#       if op == 'p' or op == 'P':
#         player.PurchaseFromShop(shop)
#       elif op == 'r' or op == 'R':
#         player.Restock(shop)
#       elif op == 'h' or op == 'H':
#         player.healSelf()
#       else:
#         print('Invalid key. Retry')
#         continue

  
#   def nightActivity():
#     gmv.nightCount += 1
#     print('Boo 👻 it\'s Nightime') #todo: generate random quotes




  
#   while gmv.nightCount <= 3 and player.health != 0:
#     if gmv.day:
#       dayActivity()
#     else:
#       nightActivity()
#       if gmv.nightCount == 3:
#         break 
    
#     time.sleep(gmv.duration)
#     gmv.day = not gmv.day 
  


from Character.human import Human
from Shop.daShop import Shop
from Enemy.enemy import Zombie

h = Human('name')
sh = Shop('711')
z = Zombie('Zodd 🧟‍♂️')
h.PurchaseFromShop(sh)
z.Attack(h)
h.Attack(z)
h.Attack(z)
h.Attack(z)
h.Attack(z)
h.Attack(z)

 





# from Tools.tools import Tool
# from Character.human import Human
# from Shop.daShop import Shop
# from Enemy.enemy import Zombie

# kni = Tool(0,'Knife','Weapon')
# axe = Tool(1, 'Axe', 'Weapon')
# sword = Tool(2, 'Sword', 'Weapon')
# h = Tool(3, 'Heal', 'Heal')

# print(kni,axe,sword,h)

# amy = Human('Ameya')
# sh = Shop('7/11')
# print('Coins :', amy.coins)
# amy.PurchaseFromShop(sh)
# print('Coins: ',amy.coins,' Inventory: ',amy.inventory)
# zom = Zombie('Zom')
# zom.Attack(amy)
# amy.Attack(zom)
# print('Zom and Amy healths after attack resp.',zom.health,amy.health)

# amy.Restock(sh)
# print('Effect after restocking ', sh.stock)