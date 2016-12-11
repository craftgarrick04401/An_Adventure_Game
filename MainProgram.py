from CreatureClass import Creature
from ItemClass import *
from MapClass import Map
from random import randint, choice
from time import sleep

def developer():
    
    map1 = Map('Abandoned Building', 10, 5)
    
    uinput = 0
    actions = []
    
    while uinput != 'q':
        
        map1.show()
        
        uinput = input("map action...").lower()
    
        if uinput == 'r':
            x1 = int(input("X1..."))
            y1 = int(input("Y1..."))
            x2 = int(input("X2..."))
            y2 = int(input("Y2..."))
            brush = input("Brush...")
            
            map1.drawRect(x1, y1, x2, y2, brush)
            actions.append(['rect:', x1, y1, x2, y2, brush, map1.layer])
            
        elif uinput == 'l':
            x1 = int(input("X1..."))
            y1 = int(input("Y1..."))
            x2 = int(input("X2..."))
            y2 = int(input("Y2..."))
            brush = input("Brush...")
            
            map1.drawLine(x1, y1, x2, y2, brush)
            actions.append(['line:', x1, y1, x2, y2, brush, map1.layer])
            
        elif uinput == 'p':
            x = int(input("X1..."))
            y = int(input("Y1..."))
            brush = input("Brush...")
            
            map1.drawPoint(x, y, brush)
            actions.append(['point:', x, y, brush, map1.layer])
            
        elif uinput == 'c':
            layer = int(input("Jump to Layer..."))
            
            map1.changeLayer(layer - map1.layer)
        
        
    for i in actions:
        print(i)
        
def encounter(player, opponent):
    
    if player.initiative > opponent.initiative:
        
        first = player.name
        
    elif opponent.initiative > player.initiative:
        
        first = opponent.name
        
    else:
        
        first = choice([player.name, opponent.name])
        
    while player.alive and opponent.alive:
        
        sleep(0.5)
        
        if first == player.name:
            
            wfi(True, player=player, opponent=opponent)
            sleep(0.5)
            
            if player.alive and opponent.alive:
                
                opponent.playStatus()
                sleep(0.5)
                player.hurt(opponent.rollAttack())
            
        else:
            
            player.hurt(opponent.rollAttack())
            sleep(0.5)
            
            if player.alive and opponent.alive:
                
                wfi(True, player=player, opponent=opponent)
                sleep(0.5)
                opponent.playStatus()
        
def wfi(danger=False, player=False, opponent=False):
    
    while 1:
        
        if danger:
            
            uinput = input("What 'WILL' you do? (attack, inventory, status)").lower()
            
            if uinput == 'a' or uinput == 'attack':
                
                opponent.hurt(player.rollAttack())
                break
            
            elif uinput == 'inv' or uinput == 'inventory':
                pass
            elif uinput == 's' or uinput == 'status':
                
                print("\n%s: Hp = %s, Attack = %s, Defense = %s\n" %(player.name, player.hp, player.attack, player.defense))
            
        else:
            
            uinput = input("What 'Will' you do? (inventory, character, map, move)").lower()
        
            if uinput == 'inv' or 'inventory':
                pass
            elif uinput == 'char' or 'character':
                pass
            elif uinput == 'map':
                pass
            elif uinput == 'move':
                pass

if __name__ == '__main__':
    
    player = Creature('player', initiative=5, hp=30, attack=5, defense=3)
    monster = Creature('monster', attack=7, hp=16)
    
    encounter(player, monster)
        

                
                
                
                
                
