class Item(object):
    def __init__(self, itemName, value):
        itemType = 'Item'
        self.properties = {
            'itemName': itemName,
            'value': value,
            'amount': 1,
            }
    def getItemProperties(self):
        return self.properties
        
    def getItemType(self):
        return self.itemType

class Equippable(Item):
    def __init__(self, itemName, value, attack, defense, slot):
        Item.__init__(self, itemName, value)
        self.itemType = 'equippable'
        self.properties['attack'] = attack
        self.properties['defense'] = defense
        self.properties['slot'] = slot
        self.properties['equipped'] = False
        

class Usable(Item):
    def __init__(self, itemName, value):
        Item.__init__(self, itemName, value)
        self.itemType = 'Usable'
        self.properties['usable'] = True

class Junk(Item):
    def __init__(self, itemName, value):
        Item.__init__(self, itemName, value)
        self.itemType = 'Junk'
