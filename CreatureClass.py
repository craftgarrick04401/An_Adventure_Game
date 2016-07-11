from random import randint
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
            'Equippable': [],
            'Usable': [],
            'Junk': []
            }
        self.slots = {
            'MainHand': '(none)',
            'OffHand': '(none)',
            'Chest': '(none)',
            'Head': '(none)',
            'Legs': '(none)',
            'Feet': '(none)'
            }
        
    def add(self, itemType, itemProperties):

        if itemType == 'Item':
            self.bag['Items'].append(itemProperties)
        if itemType == 'Equippable':
            itemProperties['tag'] = randint(0, 1000)
            conflictingTag = [x['tag'] for x in self.bag[itemType]]
            if not conflictingTag == []:
                while conflictingTag[0] == itemProperties['tag']:
                    itemProperties['tag'] = randint(0, 1000)
            self.bag['Equippable'].append(itemProperties)
        if itemType == 'Usable':
            self.bag['Usable'].append(itemProperties)
        else:
            self.bag['Junk'].append(itemProperties)
        print(itemType)
    
    def inv(self):
        print('_' * 40)
        print(" ")
        print(self.name + ':')
        print(" ")
        print("-----Inventory-----")
        print(" ")
        print("Items:")
        print(" ")
        if self.bag['Items'] == []:
            print("    (none)")
        else:
            for i in self.bag['Items']:
                print("Name: " + i['itemName'], "Value: " + i['value'])
        print(" ")
        print("Equippable:")
        print(" ")
        if self.bag['Equippable'] == []:
            print("    (none)")
        else:
            for i in self.bag['Equippable']:
                if i['equipped']:
                    print("Name:" + i['itemName'], "Value: " + i['value'], "Atk: " + i['attack'], "Def: " + i['defense'], "(equipped)")
                else:
                    print("Name:" + i['itemName'], "Value: " + i['value'], "Atk: " + i['attack'], "Def: " + i['defense'])
        print(" ")
        print("Usable:")
        print(" ")
        if self.bag['Usable'] == []:
            print("    (none)")
        else:
            for i in self.bag['Usable']:
                print("Name: " + i['itemName'], "Amount: " + i['amount'], "Value: " + i['value'], "Use: " + i['useDescription'])
        print(" ")
        print("Junk:")
        print(" ")
        if self.bag['Junk'] == []:
            print("    (none)")
        else:
            for i in self.bag['Junk']:
                print("Name: " + i['itemName'], "Value: " + i['value'])
        print(" ")
        print("_" * 40)    
        
    def stats(self):
        print('_' * 40)
        print(" ")
        print(self.name + ':')
        print(" ")
        print("-----Stats-----")
        print(" ")
        print("    Hp: " + str(self.hp))
        print("    Attack: " + str(self.attack))
        print("    Defense:" + str(self.defense))
        print(" ")
        print("-----Gear-----")
        print(" ")
        for i in self.slots:
            print(i + ":    " + self.slots[i])
        print(" ")
        print("_" * 40)

    def configureStats(self):
        total_attack = [x['attack'] for x in self.bag['Equippable'] if x['equipped'] == True]
        total_defense = [x['defense'] for x in self.bag['Equippable'] if x['equipped'] == True]
        self.attack = self.baseAttack
        self.defense = self.baseDefense
        for a, b in zip(total_attack, total_defense):
            self.attack += a
            self.defense += b

    def unequip(self, itemName):
        item = [x for x in self.bag['Equippable'] if x['equipped'] and itemName == x['itemName']]
        if item == []:
            print("Item was not found, or was already unequipped.")
        else:
            item = item[0]
            self.slots[item['slot']] = '(none)'
            for i in self.bag['Equippable']:
                if i == item:
                    i['equipped'] = False
            print("%s unequipped %s!" %(self.name, itemName))
        
    def equip(self, itemName):
        item = [x for x in self.bag['Equippable'] if not x['equipped'] and itemName == x['itemName']]
        if item == []:
            print("Item was not found, or was already equipped.")
        else:
            item = item[0]
            if self.slots[item['slot']] != '(none)':
                self.unequip(self.slots[item['slot']])
            for i in self.bag['Equippable']:
                if i == item:
                    i['equipped'] = True
                    self.slots[i['slot']] = i['itemName']
                    break
            self.configureStats()
            print("%s equipped %s!" %(self.name, itemName))
                    
            
            
        
        
        
        
        
        
        
