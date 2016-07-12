from random import randint
class Creature(object):
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.alive = True
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
    
    def checkBag(self, itemName):
        checkItems = [x for x in self.bag['Items'] if itemName == x['itemName']]
        checkEquippable = [x for x in self.bag['Equippable'] if itemName == x['itemName'] and x['equipped']]
        checkUsable = [x for x in self.bag['Usable'] if itemName == x['itemName']]
        checkJunk = [x for x in self.bag['Junk'] if itemName == x['itemName']]
        item = [checkEquippable, checkItems, checkJunk, checkUsable]
        for i in range(len(item)):
            if item[i] != []:
                item = item[i][0]
                break
        else:
            item = []
        return item
        
    def add(self, itemProperties):
        item = self.checkBag(itemProperties['itemName'])
        if item == []:
            itemType = itemProperties['itemType']
            if itemType == 'Items':
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
            if itemType == 'Junk':
                self.bag['Junk'].append(itemProperties)
        else:
            for i in self.bag[item['itemType']]:
                if i == item:
                    i['amount'] += 1
                    break
            
    
    def addAmount(self, itemProperties, amount):
        for i in range(amount):
            self.add(itemProperties)
    
    def remove(self, itemName):
        item = self.checkBag(itemName)
        if item == []:
            print("Item was not found, or was equipped.")
        else:
            for i in range(len(self.bag[item['itemType']])):
                if self.bag[item['itemType']][i] == item:
                    if item['amount'] > 1:
                        self.bag[item['itemType']][i]['amount'] -= 1
                    else:
                        del self.bag[item['itemType']][i]
                    break
                
    def removeAmount(self, itemName, amount):
        for i in range(amount):
            self.remove(itemName)

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
                print("    " + i['itemName'] + ':',"Amount: " + str(i['amount']), "Value: " + str(i['value']))
        print(" ")
        print("Equippable:")
        print(" ")
        if self.bag['Equippable'] == []:
            print("    (none)")
        else:
            for i in self.bag['Equippable']:
                if i['equipped']:
                    print("    " + i['itemName'] + ':', "Value: " + str(i['value']), "Atk: " + str(i['attack']), "Def: " + str(i['defense']), "Slot: " + i['slot'], "(equipped)")
                else:
                    print("    " + i['itemName'] + ':', "Value: " + str(i['value']), "Atk: " + str(i['attack']), "Def: " + str(i['defense']), "Slot: " + i['slot'])
        print(" ")
        print("Usable:")
        print(" ")
        if self.bag['Usable'] == []:
            print("    (none)")
        else:
            for i in self.bag['Usable']:
                print("    " + i['itemName'] + ':', "Amount: " + str(i['amount']), "Value: " + str(i['value']), "Use: " + i['useDescription'])
        print(" ")
        print("Junk:")
        print(" ")
        if self.bag['Junk'] == []:
            print("    (none)")
        else:
            for i in self.bag['Junk']:
                print("    " + i['itemName'] + ':', "Value: " + str(i['value']))
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
            
    def takingDamage(self, amount):
        if amount != False:
            if self.defense > amount:
                amount = 0
            else:
                amount -= self.defense
            if amount > self.hp:
                self.hp = 0
                self.alive = 0
            else:
                self.hp -= amount
            print("%s takes %s damage!" &(self.name, amount))
        else:
            pass
            
    def rollAttack(self):
        attack = self.attack
        attackModifier = randint(1, 21)
        if attackModifier == 20:
            print("Critical Hit!")
            attack *= 2
            print()
            return attack
        elif(attackModifier == 1):
            print("Critical Fail!")
            self.takingDamage(attack)
            return False
        else:
            return attack
            
            
        

        
        
        
        
        
        
