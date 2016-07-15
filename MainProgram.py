from CreatureClass import Creature
from ItemClass import *
from MapClass import Map


#Maps

dm = Map('Demo Map', 20, 2)
dm.drawRect(0, 0, 19, 19, 'X')
dm.drawRect(7, 7, 11, 11, 'X')
dm.drawPoint(7, 9, ' ')
dm.drawPoint(11, 9, ' ')
dm.changeLayer(1)
dm.drawPoint(5, 5, 'H')
dm.changeLayer(-1)
maps = [dm]

#Creatures
player = Creature('Player', 1, 1, 20)

#Items

item1 = Equippable('Dagger', 10, 5, 0, 'MainHand')
item2 = Equippable('Robes', 10, 0, 3, 'Chest')
item3 = Equippable('Hood', 10, 0, 2, 'Head')
item4 = Equippable('Shoes', 7, 0, 1, 'Feet')
item5 = Equippable('Pants', 10, 0, 3, 'Legs')
startingGear = [item1, item2, item3, item4, item5]

item6 = Usable('Healing Potion', 10, "Restore 10 Hp", 'rhp', 10)

#Main Method
def main():
    while 1:
        choice = input("New Game? (Y/N)").upper()
        if choice == 'N':
            break
        if choice == 'Y':
            currentMap = 0
            choice = str(input("What is your name?"))
            player = Creature(choice, 1, 0, 20)
            for i in startingGear:
                player.add(i.getItem())
            for i in player.bag['Equippable']:
                player.equip(i['itemName'])
            player.addAmount(item6.getItem(), 10)
            
            while 1:
                choice = input("What 'Will' you do? (move, map, bag, stats, quit)").lower()
                if choice == 'map':
                    maps[currentMap].show()
                if choice == 'move':
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
                            while 1:
                                choice = str(input("Choose an item... (back)"))
                                if choice == 'back' or choice == 'b':
                                    break
                                else:
                                    player.use(choice)
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
                                    player.unequip(choice)
                        if choice == 'refresh' or choice == 'r':
                            player.stats()
                        if choice == 'back' or choice == 'b':
                            break
                if choice == 'quit' or choice == 'q':
                    break
                
                
                
                
main()
                
                
                
                
                
