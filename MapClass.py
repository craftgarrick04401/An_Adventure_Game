class Map:
    def __init__(self, name, size, layers):
        self.name = name
        self.size = size
        self.layer = 0
        self.layers = layers
        self.mapArray = [[[x for x in [' '] * layers] for x in range(size)] for x in range(size)]
    
    def show(self):
        print('Map: ' + self.name)
        print('Floor: ' + str(self.layer + 1))
        print(' ')
        print("      " + "  ".join([str(x) for x in range(self.size) if x < 10]) + "  " + " ".join([str(x) for x in range(self.size) if x >= 10]))
        for i in range(self.size):
            if i < 10:
                print("    " + str(i) + " " + "  ".join([x[self.layer] for x in [x for x in self.mapArray[i]]]))
            else:
                print("   " + str(i) + " " + "  ".join([x[self.layer] for x in [x for x in self.mapArray[i]]]))
        print(' ')
            
    def changeLayer(self, increment):
        #changes the current layer
        self.layer += increment
        
    def drawPoint(self, row, column, brush):
        #draws a point on the current layer
        self.mapArray[row][column][self.layer] = brush
        
    def drawLine(self, startRow, startColumn, endRow, endColumn, brush):
        #always left to right or up to down
        if startRow == endRow:
            for i in range((endColumn - startColumn) + 1):
                self.drawPoint(startRow, startColumn + i, brush)
        else:
            for i in range((endRow - startRow) + 1):
                self.drawPoint(startRow + i, startColumn, brush)
                
    def drawRect(self, startRow, startColumn, endRow, endColumn, brush):
        #always top left to bottom right
        self.drawLine(startRow, startColumn, endRow, startColumn, brush)
        self.drawLine(startRow, startColumn, startRow, endColumn, brush)
        self.drawLine(startRow, endColumn, endRow, endColumn, brush)
        self.drawLine(endRow, startColumn, endRow, endColumn, brush)
                
            
        