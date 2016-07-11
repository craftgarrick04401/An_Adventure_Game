from CreatureClass import Creature
from ItemClass import *
from MapClass import Map
from Items import Equippable

#Maps
"""
dm = Map('Demo Map', 20, 2)
dm.drawRect(0, 0, 19, 19, 'X')
dm.drawRect(7, 7, 11, 11, 'X')
dm.drawPoint(7, 9, ' ')
dm.drawPoint(11, 9, ' ')
dm.show()
dm.changeLayer(1)
dm.drawPoint(5, 5, 'H')
dm.show()
"""
#Creatures
player = Creature('Player', 1, 1, 20)

#Items

item1 = Equippable('Dagger', 10, 5, 0, 'MainHand')
item2 = Equippable('Robes', 10, 0, 3, 'Chest')
item3 = Equippable('Hood', 10, 0, 2, 'Head')
item4 = Equippable('Shoes', 7, 0, 1, 'Feet')
item5 = Equippable('Pants', 10, 0, 3, 'Pants')

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
                
                
                
                
                
                
                
                
                
                
