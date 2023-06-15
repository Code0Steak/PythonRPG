Goal: To develope a Role Playing Game(RPG) controlled by the user via the console. the Character/Human is the protagonist of the game. 

## Class Overview

1. Human(name, health, coins, inventory) - 

   The Character/Human class should be defined with the private attributes mentioned above(name, health,..). 
   
   Following are the methods for Human,
   
   Purchase() - navigate through 'item' in Shop. Select one then buy. If enough 'coins' then buy and add to inventory. The 'item' should be reduced from 'shop stock'. The item should be added to Human's 'inventory'

   Attack(obj) - Takes a parameter 'obj', which is an Enemy object. Attack Enemy 'obj' if 'item' of type 'Weapon' available in inventory then you can proceed with the attack. Use the 'obj's TakeDamage method to cause damage. The 'Weapon' item used from Inventory will cause that amount of damage. After damage, the 'Weapon' item's durablity should degrade. if 0 remove the Item from Inventory.

   TakeDamage(val) - health will be reduced by val amount. This function should be exposed to the entity causing damage, since the 'health' param/attribute is private. 
   
   Restock(shop) - Takes Shop object as input param. This function will be used for restocking item in shop, if sufficient coins are present.
   
   HealSelf() - If 'Heal' item is present in the inventory, this will heal the Human with the heal amount. Remember full healing will be till 100, do not exceed the 100 health mark.
   
   GetHealth() - will return health of the human.


2. Enemy(name, health, dropCoins) -
The 2 types of enemies are Zombie(150 health, 30 damage) and Vampire(200 health, 70 damage)
Attack() to attack human. TakeDamage() will be exposed, as the health attribute is private.(i.e. direct change or update to the object's health attribute should not be allowed) 
The dropCoins variable denotes the no of coins the Enemy will drop once slayed.


3. Tools(id, price, type, name) -
  Tools can be of type 'Weapon' or 'Heal'.'Knife'(50 price, deals 100 damage) and 'Axe'(99 price, deals 150 damage) are weapons. After each use the durability of tools should be reduced, design a func for the same. The items of type 'Weapon' will have 'durability' attribute. 'Heal' item will have 'healVal' attribute to heal that amounts.

4. Shop(Composed of Items) - a list of (quantity, items).  

 **Class Diagram**
  
 ![Class Diagram](/RPG-Class-Diagram.png "CD")

### Current Folder Structure
The root folder contains test.py file. To test classes/objects and their methods. 
```
python3 test.py //in your termial
```
 --test.py <br>
     &nbsp;&nbsp;&nbsp;&nbsp;| <br>
     &nbsp;&nbsp;&nbsp;&nbsp;|---Character/human.py <br>
     &nbsp;&nbsp;&nbsp;&nbsp;| <br>
     &nbsp;&nbsp;&nbsp;&nbsp;|---Enemy/enemy.py <br>
     &nbsp;&nbsp;&nbsp;&nbsp;| <br>
     &nbsp;&nbsp;&nbsp;&nbsp;|---Shop/daShop.py <br>
     &nbsp;&nbsp;&nbsp;&nbsp;| <br>
     &nbsp;&nbsp;&nbsp;&nbsp;|---Tools/tools.py
   
  The folders contain the respective class definations.

## Development Overview
The Game will be developed as per below instructions.

| Development Item     | Status |
| ----------- | ----------- |
| Develop classes as per above definitions.      | Completed     |
|Run a day and night swap loop. 5mins day, 5mins night. Spawn enemies at night. Enemies will deal constant damage per minute. Human has to kill enemies to surview.  | In-progress      |
| After death of an enemy, coins will be added to the human's a/c. If user doesn't kill enemy and survives damage, no coins will be added. the enemies will disappear in the day, if not killed. | Completed |
|The user may purchase 'med kit' to heal | Completed |
|Goal will be maximize coins and buy the 'sword' till the 3rd night to kill the boss. Spawn the boss Dracula on the 3rd night. If Human survives, Declare 'Winner'. End Game.| In-progress|

## How to Run the game?

The game uses the 'PrettyTable' library for formatting outout to the console. Make sure you have 'PrettyTable' installed using pip.

```
python -m pip install -U prettytable
```

The test.py file contains script for the game. If you are on VSCode, use the Python extention to run the test.py script. Or run the script from console using the command.:

```
python3 test.py 

```

