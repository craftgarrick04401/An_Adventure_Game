from ItemClass import Item

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
        
        else:
            
            self.inv.append(itemAttributes)
    
    def remove(self, itemName):
        
        for i in range(len(self.inv)):
            
            if self.inv[i]['ItemName'] == itemName:
                
                if self.inv[i]['Quantity'] > 1:
                    
                    self.inv[i]['Quantity'] -= 1
                    break
                
                else:
                    
                    del self.inv[i]
                    break
        
        else:
            
            print("Error: item not found")
        
if __name__ == '__main__':
    
    ex = Inventory('example', 8)
    print(ex.inv)