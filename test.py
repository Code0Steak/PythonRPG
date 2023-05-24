from Character.human import Human
from Enemy.enemy import Zombie
from Tools.tools import Axe, Knife

h1 = Human('Ameya')
z1 = Zombie('Zodd')

#zombie attacks h1
z1.Attack(h1)
#check damage
print(h1.health)

h1.Purchase(Knife())
print(h1.inventory)  #check inventory after purchase


round = 0
#use of health param, as it is should not be allowed. The below should not be permitted, health is to be declared as private yet.
while z1.health >= 0:
  round += 1
  h1.Attack(z1)
print(f'Killed in {round} rounds')
