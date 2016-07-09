class Item(object):
    def __init__(self, itemName, value):
        self.properties = {
            'itemName': itemName,
            'value': value,
            'amount': 1,
            'useable': False
            }
    def getItem(self):
        return self.properties

class Equippable(Item):
    def __init__(self, itemName, value, attack, defense, slot):
        Item.__init__(self, itemName, value)
        self.properties['attack'] = attack
        self.properties['defense'] = defense
        self.properties['slot'] = slot
        self.properties['equipped'] = False
        

class Useable(Item):
    def __init__(self, itemName, value):
        Item.__init__(self, itemName, value)
        self.properties['useable'] = True
        pass

class Junk(Item):
    def __init__(self, itemName, value):
        Item.__init__(self, itemName, value)
        pass
