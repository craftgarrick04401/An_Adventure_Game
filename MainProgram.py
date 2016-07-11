from CreatureClass import Creature
from ItemClass import *
from MapClass import Map

#Maps
dm = Map('Demo Map', 20, 2)
dm.drawRect(0, 0, 19, 19, 'X')
dm.drawRect(7, 7, 11, 11, 'X')
dm.drawPoint(7, 9, ' ')
dm.drawPoint(11, 9, ' ')

#Creatures
player = Creature('Player', 1, 1, 20)

#Items
item1 = Equippable('Sword', 0, 5, 0, 'MainHand')

print(player.bag['Equippable'])
player.stats()
player.add(item1.getItemType(), item1.getItemProperties())
player.equip('Sword')
print(player.bag['Equippable'])
player.stats()
player.unequip('Sword')
player.stats()
#Main Method
def main():
    while 1:
        choice = input("New Game? (Y/N)").upper()
        if choice == 'N':
            break
        if choice == 'Y':
            choice = str(input("What is your name?"))
            player = Creature(choice, 1, 0, 20)
            
            
            while 1:
                choice = input("What 'Will' you do? (move, bag, stats, quit)").lower()
                if choice == 'move' or choice == 'm':
                    pass
                if choice == 'bag' or choice == 'b':
                    player.inv()
                    while 1:
                        choice = input("(equip, use, refresh, back)").lower()
                        if choice == 'equip' or choice == 'e':
                            while 1:
                                choice = str(input("Choose an item... (back)"))
                                if choice == 'back' or choice == 'b':
                                    break
                                else:
                                    player.equip(choice)
                        if choice == 'use' or choice == 'u':
                            pass
                        if choice == 'refresh' or choice == 'r':
                            player.inv()
                        if choice == 'back' or choice == 'b':
                            break
                if choice == 'stats' or choice == 's':
                    player.stats()
                    while 1:
                        choice = input("(unequip, refresh, back)").lower()
                        if choice == 'unequip' or choice == 'u':
                            while 1:
                                choice = str(input("Choose an item... (back)"))
                                if choice == 'back' or choice == 'b':
                                    break
                                else:
                                    player.unequip(choice, False)
                        if choice == 'refresh' or choice == 'r':
                            player.stats()
                        if choice == 'back' or choice == 'b':
                            break
                if choice == 'quit' or choice == 'q':
                    break
                
                
                
                
                
                
                
                
                
                
