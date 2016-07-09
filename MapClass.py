class Map:
    def __init__(self, name, layers):
        self.name = name
        self.map = []
        self.brushes = {
            'wall': '[X]',
            'erase': '   ',
            'drop': '[O]',
            'player': '[Y]',
            'encounter': '[!]'
            }
        for i in range(10):
            self.map.append(['   '] * 10)
    def add(self, creaturePos, brush):
        self.map[creaturePos['row']][creaturePos['column']] = self.brushes[brush]
        
    def show(self):
        print("-" * 40)
        print(" ")
        print("Map: " + self.name)
        print(" ")
        num = 0
        numbers = []
        for i in range(10):
            numbers.append(str(num))
            num = num + 1
        print("         " + "   ".join(numbers))
        num = 0
        for i in self.map:
            print("      " + str(num) + " " + " ".join(self.map[num]))
            num = num + 1
        print(" ")
        print("-" * 40)
    def draw_point(self, brush, column, row):
        self.map[row][column] = self.brushes[brush]
        
    def draw_line(self, brush, column, row, distance, direction):
        distance += 1
        num = 0
        if direction == 'N':
            for i in range(distance):
                self.draw_point(brush, column, row - num)
                num += 1
        elif direction == 'E':
            for i in range(distance):
                self.draw_point(brush, column + num, row)
                num += 1
        elif direction == 'S':
            for i in range(distance):
                self.draw_point(brush, column, row + num)
                num += 1

        elif direction == 'W':
            for i in range(distance):
                self.draw_point(brush, column - num, row)
                num += 1
        else:
            print("draw_line() direction error")

    def draw_rect(self, brush, column1, row1, column2, row2):
        length = abs(column1 - column2)
        width = abs(row1 - row2)
        if row1 < row2:
            self.draw_line(brush, column1, row1, width, 'S')
            self.draw_line(brush, column2, row2, width, 'N')
            if column1 < column2:
                self.draw_line(brush, column1, row1, length, 'E')
                self.draw_line(brush, column2, row2, length, 'W')
            else:
                self.draw_line(brush, column1, row1, length, 'W')
                self.draw_line(brush, column2, row2, length, 'E')
        else:
            self.draw_line(brush, column1, row1, width, 'N')
            self.draw_line(brush, column2, row2, width, 'S')
            if column1 < column2:
                self.draw_line(brush, column1, row1, length, 'E')
                self.draw_line(brush, column2, row2, length, 'W')
            else:
                self.draw_line(brush, column1, row1, length, 'W')
                self.draw_line(brush, column2, row2, length, 'E')
