import random

result_matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]
result_matrix1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]
move_list = []


def complement_move(direction):
    if direction == 'w':
        return 's'
    if direction == 's':
        return 'w'
    if direction == 'a':
        return 'd'
    if direction == 'd':
        return 'a'


def scramble():
    global move_list
    matrix = result_matrix  
    for i in "abcde":        
        info_matrix = check_move(matrix)
        possible_moves = info_matrix[0]
        row, col = info_matrix[1]
        if not move_list:
            choice = random.choice(possible_moves)
            make_pseudo_move(matrix, choice, row, col)
            move_list.append(choice)
            continue
        possible_moves.remove(complement_move(move_list[-1]))
        choice = random.choice(possible_moves)
        make_pseudo_move(matrix, choice, row, col)
        move_list.append(choice)    
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for column in row:
            print(column,  end='\t')
        print('\n')
    return


def find_coordinate(matrix):    
    for row_index, row_val in enumerate(matrix):
        for col_index, col_val in enumerate(row_val):
            if col_val == ' ':                
                return [row_index, col_index]


def check_move(matrix):    
    row_index, col_index = find_coordinate(matrix)       
    legal_moves = ['w', 's', 'a', 'd']

    if row_index == 0 and col_index == 0:   # upper left corner
        legal_moves = ['w', 'a']
    if (row_index == 0 and col_index != 0) and (row_index == 0 and col_index != (len(matrix[0]) - 1)):  # upper edge
        legal_moves = ['w', 'a', 'd']
    if row_index == 0 and col_index == (len(matrix[0]) - 1):  # upper right corner
        legal_moves = ['w', 'd']
    if (row_index != 0 and col_index == 0) and (row_index != (len(matrix) - 1) and col_index == 0):  # left edge
        legal_moves = ['w', 's', 'a']
    if (row_index != 0 and col_index == (len(matrix[0]) - 1)) and (
            row_index != (len(matrix) - 1) and col_index == (len(matrix[0]) - 1)):  # right edge
        legal_moves = ['s', 'w', 'd']
    if row_index == (len(matrix) - 1) and col_index == 0:  # bottom left corner
        legal_moves = ['s', 'a']
    if (row_index == (len(matrix) - 1) and col_index != 0) and (
            row_index == (len(matrix) - 1) and col_index != (len(matrix[0]) - 1)):  # bottom edge
        legal_moves = ['s', 'd', 'a']
    if row_index == (len(matrix) - 1) and col_index == (len(matrix[0]) - 1):  # bottom right corner
        legal_moves = ['s', 'd']    
    return legal_moves, [row_index, col_index]


def make_move(matrix):

    info_matrix = check_move(matrix)
    valid_moves = info_matrix[0]
    row_index, col_index = info_matrix[1]
    move = input("enter move {} : " .format(valid_moves))
    if move.lower() == 'quit':
        exit(-1)
    elif move.lower() in valid_moves:
        make_pseudo_move(matrix, move, row_index, col_index)
        print_matrix(matrix)
    else:
        print("'{}' is not a valid move. Enter a valid move. {}".format(move, valid_moves))
        make_move(matrix)
    return


def make_pseudo_move(matrix, move, row_index, col_index):
    if move.lower() == 'w':
        temp = matrix[row_index + 1][col_index]
        matrix[row_index][col_index] = temp
        matrix[row_index + 1][col_index] = ' '
    if move.lower() == 's':
        temp = matrix[row_index - 1][col_index]
        matrix[row_index][col_index] = temp
        matrix[row_index - 1][col_index] = ' '
    if move.lower() == 'a':
        temp = matrix[row_index][col_index + 1]
        matrix[row_index][col_index] = temp
        matrix[row_index][col_index + 1] = ' '
    if move.lower() == 'd':
        temp = matrix[row_index][col_index - 1]
        matrix[row_index][col_index] = temp
        matrix[row_index][col_index - 1] = ' '
    
    return


print_matrix(result_matrix)
scramble_matrix = scramble()
print_matrix(result_matrix)
while scramble_matrix != result_matrix1:
    make_move(scramble_matrix)

