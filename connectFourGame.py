#FIX> Add error handling when player selects column that is not between 1 and 7
#Fix> Do net let player keep adding to a column when it is full


board = []
boardColumns = 7
boardRows = 6
emptySpaceValue = '_'
player1Value = 'O'
player2Value = 'N'
gameWinner = 0 # 1 when player 1 is winner, 2 when player 2 is winner

#Create board list
nRow = 0
while nRow < boardRows:
    board.append([])
    nColumn = 0
    while nColumn < boardColumns:
        board[nRow].append(emptySpaceValue)
        nColumn += 1
    nRow += 1
#print(board) 

#Display board
def display_board():
    print("\nCONNECT FOUR GAME \n")
    #display column numbers
    firstRow = ' '
    f = 0
    while f < boardColumns:
        firstRow += str(f+1) + ' '
        f += 1
    print(firstRow)
    #display board
    nRow = 0
    while nRow < boardRows:
        newRow = "|"
        nColumn = 0
        while nColumn < boardColumns:
            newRow += board[nRow][nColumn] + "|"
            nColumn += 1
        print(newRow)
        nRow += 1

#TURNS
currentPlayerTurn = 0
inputColumnChosen = None
inputRowColumnChosen = []
def next_turn():
    global currentPlayerTurn
    currentPlayerTurn += 1
    if currentPlayerTurn > 2:
        currentPlayerTurn = 1

    display_board()
    print("")
    print(player1Name if currentPlayerTurn == 1 else player2Name, "'s turn", "(player ", currentPlayerTurn, ")")
    inputColumnChosen = input("Choose a column to play:")
    for c in range(boardRows):
        row = boardRows-1-c
        column = int(inputColumnChosen)-1
        if(board[row][column] == emptySpaceValue):
            board[row][column] =  player1Value if currentPlayerTurn == 1 else player2Value
            inputRowColumnChosen.append([row, column])
            #print(inputRowColumnChosen)
            return
    

def check_if_connect_four(charToCheck):
    nInARow = 1 #how many characters in a row... starting from the last input chosen
    #get row, column index
    row = inputRowColumnChosen[len(inputRowColumnChosen)-1][0] 
    column = inputRowColumnChosen[len(inputRowColumnChosen)-1][1] 
    #print("row: ", row, "column: ", column)
    
    horizontalInARow = 0
    verticalInARow = 0
    diagonalDownInARow = 0
    diagonalUpInARow = 0

    mostInARow = 0

    #check horizontal
    for x in range(boardColumns):
        if board[row][x] == charToCheck:
            horizontalInARow += 1
            if horizontalInARow > mostInARow:
                mostInARow = horizontalInARow
        else:
            horizontalInARow = 0
    #check vertical
    for x in range(boardRows):
        if board[x][column] == charToCheck:
            verticalInARow += 1
            if verticalInARow > mostInARow:
                mostInARow = verticalInARow
        else:
            verticalInARow = 0
    #check diagonal down
    rowDif = 0
    columnDif = 0
    if row > column:
        rowDif = row - column
    else:
        columnDif = column - row
    for x in range(boardColumns):
        if x + rowDif >= boardRows or x + columnDif >= boardColumns: #skip for if outsie list index
            break
        if board[x + rowDif][x + columnDif] == charToCheck:
            diagonalDownInARow += 1
            if diagonalDownInARow > mostInARow:
                mostInARow = diagonalDownInARow
        else:
            diagonalDownInARow = 0
    #check diagonal up
    rowInverse = boardRows - 1 - row
    startRow = boardRows - 1
    startColumn = 0
    if rowInverse > column:
        startRow = row + column
    else:
        startColumn = column - rowInverse
    for x in range(boardColumns):
        if startRow - x < 0 or startColumn + x >= boardColumns : #check for out of range error
            break
        if board[startRow - x][startColumn + x] == charToCheck:
            diagonalUpInARow += 1
            if diagonalUpInARow > mostInARow:
                mostInARow = diagonalUpInARow
        else:
            diagonalUpInARow = 0

    print("Most in a row : ", mostInARow)
    if mostInARow >= 4:
        global gameWinner
        gameWinner = currentPlayerTurn

#GET PLAYER NAMES BEFORE GAME STARTS
display_board()
player1Name = input("\nPlayer 1 name:")
player2Name = input("Player 2 name:")
#GAME LOOP
while gameWinner == 0:
    next_turn()
    check_if_connect_four(player1Value if currentPlayerTurn == 1 else player2Value)
#GAME WINNER
display_board()
print("-------------PLAYER ", player1Name if currentPlayerTurn == 1 else player2Name, " has won!!!! CONGRATS!-------------")
