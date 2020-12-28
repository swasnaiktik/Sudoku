import sys

sys.path.append(".")
from sudoku.sudoku import sudokuBoard
from flask import *
import json
app = Flask(__name__)


@app.route('/')
def Sudoku():
    return render_template('GUI/gui.html')


@app.route('/css')
def css():
    return render_template('GUI/gui.css')


@app.route('/js')
def js():
    return render_template('GUI/gui.js')


@app.route('/solveSudoku', methods=['GET', 'POST'])
def solveSudoku():
    if request.method == 'POST':
        matrix = request.get_json()
        board = sudokuBoard()
        board.makeBoard(matrix['data'])
        correct = board.solve()
        return json.dumps({'data': board.board, 'correct': correct})


if __name__ == "__main__":
    app.run()
