from Character.human import Human
from Shop.daShop import Shop
from Enemy.enemy import Zombie, Vampire
from prettytable import PrettyTable
import time, asyncio, threading


class GameVars:
  def __init__(self):
    self.duration = 5 #60sec Day, 60sec Night 
    self.day = True #start with a day
    self.nightCount = 0
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

  def dayActivity(stop_event):
    print()
    print('Day') #todo: generate random day quotes
    print('Note the following keys and operations: \n')
    table = PrettyTable()
    table.field_names = ["Key","Activity"]
    table.add_rows([
        ["p","Purchase Item from Shop"],
        ["r","Restock Item in Shop"],
        ["h","Use Healing"]
    ])
    print(table)


    while not stop_event.is_set():
      print()
      op = input('Type (activity) key and ENTER:')
      if op == 'p' or op == 'P':
        player.PurchaseFromShop(shop)
      elif op == 'r' or op == 'R':
        player.Restock(shop)
      elif op == 'h' or op == 'H':
        player.healSelf()
      else:
        print('Invalid key. Retry with following options')
        print(table)
        print()
        continue

  def zombieAttack():
    z = Zombie('Zodd 🧟‍♂️')
    print(f'{z.name} has spawned. You are under attack')
    while True:
      z.Attack(player)
      time.sleep(2)

  def vampAttack():
    v = Vampire('Arabella 🧛‍♀️')
    print(f'{v.name} has spawned. You are under attack')
    while True:
      v.Attack(player)
      time.sleep(2)
      
  
  def nightActivity(stop_event):
    
    print()
    print('Boo 👻 it\'s Nightime') #todo: generate random quotes

  
    if gmv.nightCount < 3:
      zombieThread = threading.Thread(target=zombieAttack,args=())
      zombieThread.start()
    else:
      vampThread = threading.Thread(target=vampAttack,args=())
      vampThread.start()

    table = PrettyTable()
    table.field_names = ["Key","Attributes"]
    table.add_rows([
        ["p","Purchase Item from Shop"],
        ["r","Restock Item in Shop"],
        ["h","Use Healing"],
        ["a","Attack"],
    ])
    print(table)

    while not stop_event.is_set() and player.getHealth() != 0:
      print()
      op = input('Type (activity) key and ENTER:')
      if op == 'p' or op == 'P':
        print(f"Sorry, the Shop {shop.name} is closed during night-time.")
        print()
      elif op == 'r' or op == 'R':
        print(f"Sorry, the Shop {shop.name} is closed at night.")
        print()
      elif op == 'h' or op == 'H':
        player.healSelf()
      elif op == 'a' or op == 'A':
        player.Attack(obj)
      else:
        print('Invalid key. Retry with following options')
        print(table)
        print()
        continue
    
    if gmv.nightCount < 3:
      zombieThread.join()
    else:
      vampThread.join()



  day_stop_event = threading.Event()
  night_stop_event = threading.Event()




  
  while gmv.nightCount <= 3 and player.health != 0:
    if gmv.day:
        #start dayActivity in a seperate thread
        dayActivityThread = threading.Thread(target=dayActivity, args =(day_stop_event,))
        dayActivityThread.start()

        #Game Duration
        time.sleep(gmv.duration)

        #stop after gmv.duration by interrupting dayActivity()
        day_stop_event.set()

        #wait for thread to finish
        dayActivityThread.join()
        #reset
        day_stop_event.clear()

        #Interrupt and join with night activity event
        night_stop_event.set()

        if 'nightActivityThread' in locals() and nightActivityThread.is_alive():
          nightActivityThread.join()

    else:
      nightActivityThread = threading.Thread(target=nightActivity, args=(night_stop_event,))
      nightActivityThread.start()

      time.sleep(gmv.duration)
      night_stop_event.set()
      nightActivityThread.join()
      night_stop_event.clear()

      #interrupt and join dayActivity() thread if its alive.
      day_stop_event.set()
      if 'dayActivityThread' in locals() and dayActivityThread.is_alive():
        dayActivityThread.join()




    gmv.nightCount += 1
    
    gmv.day = not gmv.day 

    if not gmv.day:
     
      print('.')
      print('.')
      print('Switching to Night...')
      print('...')
      print()
    else:
      print('.')
      print('.')
      print('Switching to Day...')
      print()

  




 





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