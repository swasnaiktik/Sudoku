from sudoku.PositionValue import PositionValue


class sudokuBoard:
    def __init__(self):
        self.values = []
        self.board = []
        self.solved = False
        for i in range(1, 10):
            column = []
            for j in range(1, 10):
                column.append(0)
            self.board.append(column)

    def addValues(self, positionValue):
        i, j = positionValue.position
        val = positionValue.value
        if not (1 <= val <= 9):
            print("Error")
        self.board[i][j] = positionValue.value
        self.values.append(positionValue.position)

    def printBoard(self):
        for i in self.board:
            print(i)

    def makeBoard(self, matrix):
        indexI = 0
        for i in matrix:
            indexJ = 0
            for j in i:
                if j != '':
                    num = PositionValue((indexI, indexJ), int(j))
                    self.addValues(num)
                indexJ += 1
            indexI += 1

    def __rowCheck(self, rowNum, num):
        return num not in self.board[rowNum]

    def __columnCheck(self, columnNum, num):
        for i in range(9):
            if self.board[i][columnNum] == num:
                return False
        return True

    def __boxCheck(self, rowNum, columnNum, num):
        a = rowNum // 3
        b = columnNum // 3
        for i in range(a * 3, (a + 1) * 3):
            for j in range(b * 3, (b + 1) * 3):
                if self.board[i][j] == num:
                    return False
        return True

    def __possibility(self, row, column, i):
        return self.__rowCheck(row, i) and self.__columnCheck(column, i) and self.__boxCheck(row, column, i)

    def __backTrackPosition(self, row, column):
        if column == 0 and row == 0:
            return None
        elif column == 0:
            preColumn = 8
            preRow = row - 1
        else:
            preRow = row
            preColumn = column - 1

        return (preRow, preColumn)

    def solve(self):
        if self.solved:
            return
        self.solved = True
        row = 0
        column = 0
        start = 1
        while row != 9 or column != 0:
            if column == 8:
                NewColumn = 0
                NewRow = row + 1
            else:
                NewRow = row
                NewColumn = column + 1

            if self.board[row][column] != 0:
                row = NewRow
                column = NewColumn
                continue
            else:
                for i in range(start, 10):
                    result = self.__possibility(row, column, i)
                    if result:
                        self.board[row][column] = i
                        row = NewRow
                        column = NewColumn
                        start = 1
                        break
                else:
                    ret = self.__backTrackPosition(row, column)
                    if ret is None:
                        return 1
                    preRow, preColumn = ret
                    while (preRow, preColumn) in self.values:
                        ret = self.__backTrackPosition(preRow, preColumn)
                        if ret is None:
                            return 1
                        preRow, preColumn = ret
                    start = self.board[preRow][preColumn]
                    self.board[preRow][preColumn] = 0
                    row = preRow
                    column = preColumn
                    start = start + 1

        return 0

    def __str__(self):
        return str(self.board)
