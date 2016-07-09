from CreatureClass import Creature
from ItemClass import *
from MapClass import Map

#Maps

demoMap = Map('Demo Map')
demoMap.draw_rect('wall', 0, 0, 9, 9)
demoMap.draw_line('erase', 3, 9, 3, 'E')
demoMap.draw_line('erase', 3, 0, 3, 'E')
demoMap.draw_rect('drop', 2, 2, 7, 7)
demoMap.draw_line('erase', 4, 7, 1, 'E')
demoMap.draw_line('erase', 4, 2, 1, 'E')
demoMap.show()


#Creatures
player = Creature('Player', 1, 1, 20)

#Items
stick = Junk('Stick', 0)
print(stick.getItemType())
print(stick.getItemProperties())
player.add(stick.getItemType(), stick.getItemProperties())
print(player.bag)


def main():
    while 1:
        choice = input("New Game? (Y/N)").upper()
        if choice == 'N':
            break
        if choice == 'Y':
            pass
