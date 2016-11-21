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
        """Moves an object on the map based on the direction and amount. Directions are 'N', 'S', 'E', and 'W'."""
        if direction == 'S':
            for i in range(amount):
                if self.mapArray[row + 1][column][self.layer] == ' ':
                    self.mapArray[row + 1][column][self.layer] = self.mapArray[row][column][self.layer]
                    self.mapArray[row][column][self.layer] = ' '
                    row += 1
                else:
                    break
        if direction == 'E':
            for i in range(amount):
                if self.mapArray[row][column + 1][self.layer] == ' ':
                    self.mapArray[row][column + 1][self.layer] = self.mapArray[row][column][self.layer]
                    self.mapArray[row][column][self.layer] = ' '
                    column += 1
                else:
                    break
        if direction == 'N':
            for i in range(amount):
                if self.mapArray[row - 1][column][self.layer] == ' ':
                    self.mapArray[row - 1][column][self.layer] = self.mapArray[row][column][self.layer]
                    self.mapArray[row][column][self.layer] = ' '
                    row -= 1
                else:
                    break
        if direction == 'W':
            for i in range(amount):
                if self.mapArray[row][column - 1][self.layer] == ' ':
                    self.mapArray[row][column - 1][self.layer] = self.mapArray[row][column][self.layer]
                    self.mapArray[row][column][self.layer] = ' '
                    column -= 1
                else:
                    break
            
if __name__ == '__main__':
    testMap = Map('testMap', 20, 3)
    testMap.drawPoint(10, 10, 'X')
    testMap.drawRect(9, 9, 11, 11, 'U')
    testMap.moveObject('N', 7, 10, 10)
    testMap.show()
                
            
        