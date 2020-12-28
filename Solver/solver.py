import sys

sys.path.append(".")
from sudoku.sudoku import sudokuBoard
from sudoku.PositionValue import PositionValue
from flask import *

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
        print(request.get_json())
        return 'OK'



if __name__ == "__main__":
    app.run()
