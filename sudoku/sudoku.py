
class sudokuBoard:
    def __init__(self):
        self.values = []
        self.board = []
        for i in range(1, 10):
            column = []
            for j in range(1, 10):
                column.append(0)
            self.board.append(column)

    def addValues(self, positionValue):
        i, j = positionValue.position
        self.board[i][j] = positionValue.value
        self.values.append(positionValue)

    def printBoard(self):
        for i in self.board:
            print(i)


