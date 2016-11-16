class Map(object):
    def __init__(self, name, size, layers):
        self.name = name
        self.size = size
        self.layer = 0
        self.layers = layers
        self.mapArray = [[[x for x in [' '] * layers] for x in range(size)] for x in range(size)]
    
    def show(self):
        print('-' * 40)
        print(' ')
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
        print('-' * 40)
            
    def changeLayer(self, increment):
        """changes the current map layer by the increment passed"""
        self.layer += increment
        
    def drawPoint(self, row, column, brush):
        """draws a point on the map"""
        self.mapArray[row][column][self.layer] = brush
        
    def drawLine(self, startRow, startColumn, endRow, endColumn, brush):
        """draws a line on the map, always from left to right or up to down"""
        if startRow == endRow:
            for i in range((endColumn - startColumn) + 1):
                self.drawPoint(startRow, startColumn + i, brush)
        else:
            for i in range((endRow - startRow) + 1):
                self.drawPoint(startRow + i, startColumn, brush)
                
    def drawRect(self, startRow, startColumn, endRow, endColumn, brush):
        """draws a rectangle on the map, always from top left to bottom right"""
        self.drawLine(startRow, startColumn, endRow, startColumn, brush)
        self.drawLine(startRow, startColumn, startRow, endColumn, brush)
        self.drawLine(startRow, endColumn, endRow, endColumn, brush)
        self.drawLine(endRow, startColumn, endRow, endColumn, brush)
        
    def moveObject(self, direction, amount, row, column):
        """needs fixing"""
        if direction == 'S':
            if self.mapArray[row + 1][column][self.layer] == ' ':
                self.mapArray[row + 1][column][self.layer] = self.mapArray[row][column][self.layer]
                self.mapArray[row][column][self.layer] = ' '
                return
        if direction == 'E':
            if self.mapArray[row][column + 1][self.layer] == ' ':
                self.mapArray[row][column + 1][self.layer] = self.mapArray[row][column][self.layer]
                self.mapArray[row][column][self.layer] = ' '
        if direction == 'N':
            for i in range(amount):
                if self.mapArray[row - 1][column][self.layer] == ' ':
                    self.mapArray[row - 1][column][self.layer] = self.mapArray[row][column][self.layer]
                    self.mapArray[row][column][self.layer] = ' '
                else:
                    break
                row += 1
        if direction == 'W':
            if self.mapArray[row][column - 1][self.layer] == ' ':
                self.mapArray[row][column - 1][self.layer] = self.mapArray[row][column][self.layer]
                self.mapArray[row][column][self.layer] = ' '
            
if __name__ == '__main__':
    testMap = Map('testMap', 20, 3)
    testMap.drawRect(5, 10, 10, 17, 'X')
    testMap.moveObject('N', 4, 5, 10)
    testMap.show()
                
            
        