
def findEmptySpace(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:  # 0 represents empty space
                return row, column

    return None, None  # if all rows are filled.


def isValid(puzzle, guess, row, col):

    # checking row
    rowValues = puzzle[row]
    if guess in rowValues:
        return False

    # checking column
    columnValues = []
    for r in range(9):
        columnValues.append(puzzle[r][col])
    if guess in columnValues:
        return False

    # checking the 3x3 square
    row_begin = (row // 3) * 3
    col_begin = (col // 3) * 3  # indicates the box of square

    for r in range(row_begin, row_begin + 3):
        for c in range(col_begin, col_begin + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def sudokuSolver(puzzle):

    row, col = findEmptySpace(puzzle)  # finding empty space
    if row is None:  # no empty spots
        return True

    # making a guess to add number in empty space
    for guess in range(1, 10):
        if isValid(puzzle, guess, row, col):  # checking if guess is valid
            puzzle[row][col] = guess  # placing the guess in board
            if sudokuSolver(puzzle):  # looping till the board is filled
                return True

        puzzle[row][col] = 0  # backtracking when there is violation

    return False  # case when the puzzle is unsolvable.


board = [
    [5, 3, 0,   0, 7, 0,   0, 0, 0],
    [6, 0, 0,   1, 9, 5,   0, 0, 0],
    [0, 9, 8,   0, 0, 0,   0, 6, 0],

    [8, 0, 0,   0, 6, 0,  0, 0, 3],
    [4, 0, 0,   8, 0, 3,  0, 0, 1],
    [7, 0, 0,   0, 2, 0,  0, 0, 6],

    [0, 6, 0,   0, 0, 0,  2, 8, 0],
    [0, 0, 0,   4, 1, 9,  0, 0, 5],
    [0, 0, 0,   0, 8, 0,  0, 7, 9]
]
