import sys
sys.path.append(".")
from sudoku.sudoku import sudokuBoard
from sudoku.PositionValue import PositionValue

if __name__ == '__main__':
    board = sudokuBoard()
    input_ = [
        [8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]
    ]
    for i in range(9):
        for j in range(9):
            num = input_[i][j]
            if num == 0:
                continue
            else:
                board.addValues(PositionValue((i, j), num))
    board.solve()
    board.printBoard()

