from ItemClass import Item, Equipment

class Inventory(object):
    
    def __init__(self, name):
        
        self.name = name
        self.inv = []
        
    def add(self, itemAttributes, amount=1):            
        
        for i in self.inv:
            
            if i['ItemName'] == itemAttributes['ItemName']:
                
                i['Quantity'] += amount
                break
        
        else:
            
            self.inv.append(itemAttributes)
            self.add(itemAttributes, amount=amount)
    
    def remove(self, itemName, amount=1):
        
        for i in range(len(self.inv)):
            
            if self.inv[i]['ItemName'] == itemName:
                
                if self.inv[i]['Quantity'] > amount:
                    
                    self.inv[i]['Quantity'] -= amount
                    break
                
                else:
                    
                    del self.inv[i]
                    break
        
        else:
            
            print("Error: item not found")
            
    def removeAll(self):
        
        self.inv = []
            
    def show(self):
        
        print(self.name + ":\n")
        
        if self.inv != []:
            
            for i in self.inv:
            
                print(">>>>", i['ItemName'], str(i['Quantity']) + 'x:    Value:', i['ItemValue'] * i['Quantity'], '\n')
                
                if i['Equipped'] != 'unable':
                    
                    print("        Slot:", i['EquipSlot'])
                    
                    if i['Attack'] > 0:
                        
                        if i['Defense'] > 0:
                            
                            print("        Attack:", i['Attack'], "Defense:", i['Defense'])
                            
                        else:
                            
                            print("        Attack:", i['Attack'])
                            
                    elif i['Defense'] > 0:
                        
                        print("        Defense:", i['Defense'])
                         
                    print('\n')
                    
        else:
            
            print("    (none)\n")
        
if __name__ == '__main__':
    
    chest = Inventory('Chest')
    
    knife = Equipment('Knife', 5, 'MainHand', attack=5)
    shield = Equipment('Shield', 7, 'OffHand', defense=10)
    rock = Equipment('Rock', 0, 'MainHand')
    spikedShield = Equipment('Spiked Shield', 17, 'OffHand', attack=3, defense=12)
    
    chest.add(knife.get())
    chest.add(shield.get())
    chest.add(rock.get(), amount=5)
    chest.add(spikedShield.get())
    
    chest.show()
    chest.removeAll()
    chest.show()