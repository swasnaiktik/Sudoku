function makeHTML(text){
    dataP = JSON.parse(text)
    correct =  dataP.correct
    data = dataP.data
    if(correct == '1'){
        return "Sorry wrong matrix inputted"
    }
    returnHTML = '<table id = "result" border = "1px">'
    for(i = 0; i < 9; i++){
        row = '<tr>'
        for(j = 0; j < 9; j++){
            row+=('<td>'+JSON.stringify(data[i][j])+'</td>')
        }
        row+='</tr>'
        returnHTML+=row
    }
    returnHTML+='</table>'
    return returnHTML
}

function clickSolve(){
     returnMatrix = getSudokuData()
     document.getElementById("solving").disabled = true;
     fetch('/solveSudoku', {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
        "data": returnMatrix})
    }).then(function (response) {
        return response.text();
        }).then(function (text) {
        insertHTML = makeHTML(text)
        document.getElementById('solved').innerHTML = insertHTML
        document.getElementById("solving").disabled = false;
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