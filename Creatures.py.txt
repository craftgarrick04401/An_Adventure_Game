class Creature(object):
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.baseAttack = attack
        self.attack = attack
        self.baseDefense = defense
        self.defense = defense
        self.hp = hp
        self.bag = {
            'items': [],
            'equippable': [],
            'useable': [],
            'other': []
            }
        self.slots = {
            'MainHand': 'none',
            'OffHand': 'none',
            'Chest': 'none',
            'Head': 'none',
            'Legs': 'none',
            'Feet': 'none'
            }
    def add(self, item):
        if __name__.item is __name__.Item:
            self.bag['items'].append(item.properties)
        elif item is Equippable:
            self.bag['equippable'].append(item.properties)
        elif item is Useable:
            self.bag['useable'].append(item.properties)
        else:
            print(item)
            self.bag['other'].append(item.properties)

    def configure_stats(self):
        total_attack = [x['attack'] for x in self.bag['equippable'] if x['equipped'] == True]
        total_defense = [x['defense'] for x in self.bag['equippable'] if x['equipped'] == True]
        self.attack = baseAttack
        self.defense = baseDefense
        for a, b in zip(total_attack, total_defense):
            self.attack += a
            self.defense += b

    def unequip(itemName):
        for i in self.bag['equippable']:
            if i['itemName'] == itemName:
                i['equipped'] = False
                self.configure_stats()
                break
        else:
            print('Item was not equipped')
