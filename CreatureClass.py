class Creature(object):
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.baseAttack = attack
        self.attack = attack
        self.baseDefense = defense
        self.defense = defense
        self.hp = hp
        self.bag = {
            'Items': [],
            'Equipable': [],
            'Usable': [],
            'Junk': []
            }
        self.slots = {
            'MainHand': 'none',
            'OffHand': 'none',
            'Chest': 'none',
            'Head': 'none',
            'Legs': 'none',
            'Feet': 'none'
            }
    def add(self, itemType, itemProperties):
        if itemType == 'Item':
            self.bag['Items'].append(itemProperties)
        if itemType == 'Equipable':
            self.bag['Equipable'].append(itemProperties)
        if itemType == 'Usable':
            self.bag['Usable'].append(itemProperties)
        else:
            self.bag['Junk'].append(itemProperties)

    def configure_stats(self):
        total_attack = [x['attack'] for x in self.bag['equipable'] if x['equipped'] == True]
        total_defense = [x['defense'] for x in self.bag['equipable'] if x['equipped'] == True]
        self.attack = baseAttack
        self.defense = baseDefense
        for a, b in zip(total_attack, total_defense):
            self.attack += a
            self.defense += b

    def unequip(itemName):
        for i in self.bag['equipable']:
            if i['itemName'] == itemName:
                i['equipped'] = False
                self.configure_stats()
                break
        else:
            print('Item was not equipped')
