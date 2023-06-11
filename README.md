Goal: To develope a Role Playing Game(RPG) controlled by the user via the console. the Character is the protagonist of the game. 

## Class Overview

1. Character(name, health, coins, inventory) - 

   The Character/Human class should be defined with the private attributes mentioned above(name, health,..). 
   
   Following are the methods for Human,
   
   Purchase() - navigate through 'item' in Shop. Select one then buy. If enough 'coins' then buy and add to inventory. The 'item' should be reduced from 'shop stock'. The item should be added to Human's 'inventory'

   Attack(obj) - Takes a parameter 'obj', which is an Enemy object. Attack enemy 'obj'. if 'item' of type 'Weapon' avlb in inventory then you can proceed with the attack. use the 'obj's Takedamage method to cause damage. The weapon Item used from Inventory will cause that amount of damage. After damage, the 'Weapon' item's durablity should degrade. if 0 remove the Item from Inventory.

   TakeDamage(val) - health will be reduced by val amount. This function should be exposed to the entity causing damage, since the 'health' param/attribute is private.


2. Enemy(name, health) -
The 2 types of enemies are Zombie(150 health, 30 damage) and Vampire(200 health, 70 damage)
Attack() to attack human. TakeDamage() will be exposed, as the health attribute is private.(i.e. direct change or update to the object's health attribute should not be allowed)


3. Tools(price, damage caused, durability) -
  Tools can be of type 'Weapon' or 'Heal'.'Knife'(50 price, deals 100 damage) and 'Axe'(99 price, deals 150 damage) are weapons. After each use the durability of tools should be reduced, design a func for the same.

4. Shop(Composed of Items) - a list of (quantity, items). Implement restock function. Restock(val, obj) should accept value and tool(object) to be restocked by Human, if sufficient value is given, the tool should be restocked. 

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
