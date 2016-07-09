from Creatures import Creature
from Items import *

#Junk
uselessStick = Junk('Useless Stick', 0)
bagOfSand = Junk('Bag Of Sand', 0)

you = Creature


def main():
    while 1:
        choice = input("New Game? (Y/N)").upper()
        if choice == 'N':
            break
        if choice == 'Y':
            pass
