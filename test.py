from Character.human import Human
from Shop.daShop import Shop
import time, asyncio


class GameVars:
  def __init__(self):
    self.dnCyc = 2 #2min Day Night Cycle
    self.day = True #start with a day
    self.dayCount = 0
    self.gameStartTime = time.time() 
    self.gameWon = False #to load stats accordingly





if __name__ == '__main__':
  print('GAME STARTS...\n\n')
  _username = input('Type in a Username: ')
  player = Human(_username)
  gmv = GameVars()
  shop = Shop('7/11')
  print(f'\n\nCharacter {player.name} created. Some Game Variables declared...')
  print(f'Hey, {player.name}! Welcome to the Game. The following Instructons might come in handy, please go through them and hit ENTER once done.\n')
  print(f'1. The Goal of the game is \'Survival\'......')
  rw = input() #the game will start after the user hits ENTER

  #game loop
  
    

    


  
  
    
 





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