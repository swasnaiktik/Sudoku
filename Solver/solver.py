import sys
sys.path.append(".")
from sudoku.sudoku import sudokuBoard
from sudoku.PositionValue import PositionValue

def rowCheck(board, rowNum, num):
    return num not in board.board[rowNum]

def columnCheck(board, columnNum, num):
    listNum = []
    for i in range(9):
        listNum.append(board.board[i][columnNum])
    return num not in listNum

def boxCheck(board, rowNum, columnNum, num):
    a = rowNum//3
    b = columnNum//3
    listNum = []
    for i in range(a*3, (a+1)*3):
        for j in range(b*3, (b+1)*3):
            listNum.append(board.board[i][j])

    return num not in listNum

def possibility(board, row, column, i):
    return rowCheck(board, row, i) and columnCheck(board, column, i) and boxCheck(board, row, column, i)

def backTrackPosition(row, column):
    if column == 0 and row == 0:
        return None
    elif column == 0:
        preColumn = 8
        preRow = row - 1
    else:
        preRow = row
        preColumn = column - 1

    return (preColumn, preRow)


def solver(boardInUse, row, column, start=1):
    if row == 9 and column == 0:
        return boardInUse
    else:
        if column == 8:
            NewColumn = 0
            NewRow = row + 1
        else:
            NewRow = row
            NewColumn = column + 1

        if boardInUse.board[row][column] != 0:
            return solver(boardInUse, NewRow, NewColumn)
        else:
            for i in range(start, 10):
                result = possibility(boardInUse, row, column, i)
                if result:
                    boardInUse.board[row][column] = i
                    return solver(boardInUse, NewRow, NewColumn)
            else:
                preColumn, preRow = backTrackPosition(row, column)
                while (preColumn, preRow) in boardInUse.values:
                    preColumn, preRow = backTrackPosition(preRow, preColumn)
                start = boardInUse.board[preRow][preColumn]
                boardInUse.board[preRow][preColumn] = 0
                return solver(boardInUse, preRow, preColumn, start + 1)


if __name__ == '__main__':
    board = sudokuBoard()
    sys.setrecursionlimit(100000)
    board.addValues(PositionValue((0, 0), 5))
    board.addValues(PositionValue((1, 0), 3))
    board.addValues(PositionValue((4, 0), 7))
    board.addValues(PositionValue((0, 1), 6))
    board.addValues(PositionValue((3, 1), 1))
    board.addValues(PositionValue((4, 1), 9))
    board.addValues(PositionValue((5, 1), 5))
    board.addValues(PositionValue((1, 2), 9))
    board.addValues(PositionValue((2, 2), 8))
    board.addValues(PositionValue((7, 2), 6))
    board.addValues(PositionValue((0, 3), 8))
    board.addValues(PositionValue((4, 3), 6))
    board.addValues(PositionValue((8, 3), 3))
    board.addValues(PositionValue((0, 4), 4))
    board.addValues(PositionValue((3, 4), 8))
    board.addValues(PositionValue((5, 4), 3))
    board.addValues(PositionValue((8, 4), 1))
    board.addValues(PositionValue((0, 5), 7))
    board.addValues(PositionValue((4, 5), 2))
    board.addValues(PositionValue((8, 5), 6))
    board.addValues(PositionValue((1, 6), 6))
    board.addValues(PositionValue((6, 6), 2))
    board.addValues(PositionValue((7, 6), 8))
    board.addValues(PositionValue((3, 7), 4))
    board.addValues(PositionValue((4, 7), 1))
    board.addValues(PositionValue((5, 7), 9))
    board.addValues(PositionValue((8, 7), 5))
    board.addValues(PositionValue((4, 8), 8))
    board.addValues(PositionValue((7, 8), 7))
    board.addValues(PositionValue((8, 8), 9))
    solver(board, 0, 0).printBoard()













