class Item(object):
    def __init__(self, itemName, value):
        self.properties = {
            'itemName': itemName,
            'value': value,
            'amount': 1,
            'itemType': 'Items'
            }
    def getItem(self):
        """returns a dictionary of the item's properties"""
        return self.properties

class Equippable(Item):
    def __init__(self, itemName, value, attack, defense, slot):
        Item.__init__(self, itemName, value)
        self.properties['itemType'] = 'Equippable'
        self.properties['attack'] = attack
        self.properties['defense'] = defense
        self.properties['slot'] = slot
        self.properties['equipped'] = False
        
class Usable(Item):
    def __init__(self, itemName, value, useDescription, useType, useValue):
        Item.__init__(self, itemName, value)
        self.properties['itemType'] = 'Usable'
        self.properties['usable'] = True
        self.properties['useDescription'] = useDescription
        self.properties['useType'] = useType
        self.properties['useValue'] = useValue

class Junk(Item):
    def __init__(self, itemName, value):
        Item.__init__(self, itemName, value)
        self.properties['itemType'] = 'Junk'
