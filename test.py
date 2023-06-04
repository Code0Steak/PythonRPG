from Character.human import Human

if __name__ == '__main__':
  print('GAME STARTS...\n\n')
  _username = input('Type in a Username: ')
  player = Human(_username)
  print(f'\n\nCharacter {player.name} created. Some Game Variables declared...')




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