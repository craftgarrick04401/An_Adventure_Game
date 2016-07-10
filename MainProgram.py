from CreatureClass import Creature
from ItemClass import *
from MapClass import Map

#Maps

demoMap = Map('Demo Map', 10, 2)
demoMap.drawPoint(3, 3)
demoMap.show()
demoMap.changeLayer(1)
demoMap.drawPoint(5, 5)
demoMap.show()


player = Creature('Player', 1, 1, 20)

#Items


def main():
    while 1:
        choice = input("New Game? (Y/N)").upper()
        if choice == 'N':
            break
        if choice == 'Y':
            pass
