from InventoryClass import Inventory
from ItemClass import *
from random import randint

class Creature(object):
    
    def __init__(self, name, initiative=3, hp=10, attack=0, defense=0):
        
        self.alive = True
        self.name = name
        self.baseHp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.initiative = initiative
        self.bag = Inventory(name)
        
        self.slots = {
            "MainHand": '(none)',
            "OffHand": '(none)',
            "Head": '(none)',
            "Chest": '(none)',
            "Legs": '(none)',
            "Feet": '(none)'
        }
        
    def heal(self, amount):
        
        self.hp += amount
        
        if self.hp > self.baseHp:
            
            self.hp = self.baseHp
        
    def hurt(self, amount):
        
        if amount == False:
            
            pass
        
        elif amount > self.defense:
            
            amount = amount - self.defense
            self.hp -= amount
            
            print("%s takes %s damage." %(self.name, amount))
            
            if self.hp <= 0:
            
                self.hp = 0
                self.alive = False
                
                print(self.name + " has been slain!")
        else:
            
            print(self.name + " takes 0 damage.")

    def rollAttack(self):
        
        roll = randint(1, 21)
        
        if roll > 1:
            
            if roll < 20:
                
                if roll >= 10:
                    
                    return self.attack
                
                else:
                    
                    print("Missed.")
                    return False
                
            else:
                
                print("Critical Hit!")
                
                return self.attack * 2
            
        else:
            
            print("Critical Fail!")
            
            self.hurt(self.attack)
            
            return False
            
    def unequip(self, itemName):
        
        for i in self.slots:
            
            if self.slots[i] == itemName:
                
                self.slots[i] = '(none)'
                
                for x in self.bag.inv:
                    
                    if x['ItemName'] == itemName:
                        
                        x['Equipped'] = False
                        break
            
            break
        
        else:
            
            print("Item not found.")
                                          
    def equip(self, itemName):
        
        for i in self.bag.inv:
            
            if i['ItemName'] == itemName:
                
                if self.slots[i['EquipSlot']] == '(none)':
                    
                    i['Equipped'] = True
                    self.slots[i['EquipSlot']] = itemName
                    break
                
                else:
                    
                    self.unequip(self.slots[i['EquipSlot']])
                    break
                    
        else:
            
            print("Item not found.")
                
    def add(self, itemAttributes):
        
        self.bag.add(itemAttributes)
    
    def remove(self, itemName):
        
        for i in range(len(self.bag.inv)):
            
            if self.bag.inv[i]['ItemName'] == itemName:
                
                if self.bag.inv[i]['Quantity'] > 1:
                    
                    self.bag.inv[i]['Quantity'] -= 1
                    break
                
                else:
                
                    if self.bag.inv[i]['Equipped'] == True:
                        
                        self.unequip(itemName)
                    
                    del self.bag.inv[i]
                    break
        
        else:
            
            print("Item not found.")
                
    def playStatus(self):
        
        if (self.hp / self.baseHp) > (2/3):
            
            print(self.name + " seems healthy")
            
        elif (self.hp / self.baseHp) > (1/3):
            
            print(self.name + " has minor injuries")
            
        else:
            
            print(self.name + " is seriously injured")
    
if __name__ == '__main__':
    
    ex = Creature('example')
    rock = Equipment('rock', 0, 'MainHand', attack=5)
    ex.add(rock.get())
    print(ex.bag.inv)
    ex.equip('rock')
    print(ex.slots)
    print(ex.bag.inv)
    ex.remove('rock')
    print(ex.slots)
    print(ex.bag.inv)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    