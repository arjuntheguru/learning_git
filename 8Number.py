# Project to create the 8-Number slide game
# TO-DO:
# make a scramble function to scramble original matrix and make a puzzle out of it
# figure out how the fuck your supposed to interface the stdio
# make algorithm for check_move

original_matrix = [['0', '0', '0', '0'], ['0', '1', '2', '3'], ['0', '4', '5', '6'], ['0', '7', '8', ' ']]

# print_Matrix() function to print the tile puzzle


def print_matrix(matrix):
    row = 1
    while row <= 3:
        column = 1
        while column <= 3:
            print(matrix[row][column], end='\t')
            column += 1
        print('\n')
        row += 1

    return

# move() function to take input move; right now u, l, d, r = up, down, left, right
# Basically what happens is that move will first check_move to get set of valid moves then make_move


def move():
    info_matrix = check_move(original_matrix)
    temp_arr1 = info_matrix[0]
    temp_arr2 = info_matrix[1]
    move_input = input("enter move {}: ".format(temp_arr1))
    try:
        a = temp_arr1.index(move_input.lower())
    except ValueError:
        print("Enter a valid move\n")
        a = -1

    if a > -1:
        make_move(temp_arr2, move_input.lower())
    return

# make_move() function to make the actual move


def make_move(position, direction):
    row, column = position[0], position[1]
    print(row)
    print(column)
    print("original matrix: ")
    print_matrix(original_matrix)
    matrix = original_matrix
    if direction == 'u':
        temp = matrix[row][column]
        matrix[row][column] = matrix[row - 1][column]
        matrix[row - 1][column] = temp

    if direction == 'd':
        temp = matrix[row][column]
        matrix[row][column] = matrix[row + 1][column]
        matrix[row + 1][column] = temp

    if direction == 'l':
        temp = matrix[row][column]
        matrix[row][column] = matrix[row][column - 1]
        matrix[row][column - 1] = temp

    if direction == 'r':
        temp = matrix[row][column]
        matrix[row][column] = matrix[row][column + 1]
        matrix[row][column + 1] = temp

    print("matrix with values swapped")
    print_matrix(matrix)
    return

# get_position function to get position of the blank tile


def get_position(matrix, value):
    row_num = 1
    count = 0
    for row in matrix:
        count += 1
        if count == 1:
            continue
        try:
            pos = row.index(str(value))

        except ValueError:
            row_num += 1
            continue
        break

    column_num = pos
    position = [row_num, column_num]
    return position

# check_move function to check for the list of legal moves available for the blank tile's position
# right now hard coded every move 'cause matrix is small(3x3). Need to make algorithm for check_move


def check_move(matrix):
    legal_moves = []
    a = get_position(matrix, ' ')
    if a == [1, 1]:
        legal_moves = ['d', 'r']
    if a == [1, 2]:
        legal_moves = ['d', 'l', 'r']
    if a == [1, 3]:
        legal_moves = ['d', 'l']
    if a == [2, 1]:
        legal_moves = ['u', 'd', 'r']
    if a == [2, 2]:
        legal_moves = ['u', 'd', 'l', 'r']
    if a == [2, 3]:
        legal_moves = ['u', 'd', 'l']
    if a == [3, 1]:
        legal_moves = ['u', 'r']
    if a == [3, 2]:
        legal_moves = ['u', 'l', 'r']
    if a == [3, 3]:
        legal_moves = ['u', 'l']
    return [legal_moves, a]

# Lets call this part Main


print_matrix(original_matrix)

while 1:
    move()
    q = input(" ")
    if q == 'x':
        break