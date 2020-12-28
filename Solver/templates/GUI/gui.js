

function clickSolve(){
     returnMatrix = getSudokuData()
     returnMatrix = JSON.stringify(returnMatrix)
     fetch('/solveSudoku', {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'POST', body:returnMatrix
    }).then(function (response) {
        return response.text();
        }).then(function (text) {
        console.log(text)
    });
}

function getSudokuData(){
    returnMatrix = []
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for(i = 0; i < 9; i++){
        row = []
        for(j = 0; j < 9; j++){
            val = document.getElementById(letters[i]+nums[j]).value
            row.push(val)
        }
        returnMatrix.push(row)
    }
    return returnMatrix
}