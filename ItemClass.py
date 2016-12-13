class Item(object):
    
    def __init__(self, itemName, itemValue):
        
        self.itemAttributes = {
            "ItemName": '[' + itemName + ']',
            "ItemValue": itemValue,
            "Equipped": 'unable',
            "Quantity": 0
            }
    
    def get(self):
        
        return self.itemAttributes

class Equipment(Item):
    
    def __init__(self, itemName, itemValue, slot, attack=0, defense=0):
        
        Item.__init__(self, itemName, itemValue)
        
        self.itemAttributes['EquipSlot'] = slot
        self.itemAttributes['Attack'] = attack
        self.itemAttributes['Defense'] = defense
        self.itemAttributes['Equipped'] = False
        


