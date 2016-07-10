class Map:
    def __init__(self, name, size, layers):
        self.name = name
        self.size = size
        self.layer = 0
        self.layers = layers
        self.mapArray = [[[x for x in ['u'] * layers] for x in range(size)] for x in range(size)]
    
    def show(self):
        print('Map: ' + self.name)
        print('Floor: ' + str(self.layer + 1))
        print(' ')
        print("      " + " ".join([str(x) for x in range(self.size)]))
        for i in range(self.size):
            print("    " + str(i) + " " + " ".join([x[self.layer] for x in [x for x in self.mapArray[i]]]))
        print(' ')
            
    def changeLayer(self, increment):
        self.layer += increment
        
    def drawPoint(self, row, column):
        self.mapArray[row][column][self.layer] = 'h'
        