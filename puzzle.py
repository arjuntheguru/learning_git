
import random

# solved puzzle
result_matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '']]
# function to print matrix
def print_matrix(matrix):
    for row in matrix:
        for column in row:
            print(column,  end='\t')
        print('\n')
    print('\n')

# create an initial matrix with possible elements in random position
def initial_matrix():
    possible_elements = ['1','2','3','4','5','6','7','8','']
    temp1 = []
    temp2 = []
    temp3 = []
    while len(temp1) != 3:
        rand = random.choice(possible_elements)
        while rand not in temp1:
            temp1.append(rand)

    while len(temp2) != 3:
        rand = random.choice(possible_elements)
        while rand not in temp2 and rand not in temp1:
            temp2.append(rand)

    while len(temp3) != 3:
        rand = random.choice(possible_elements)
        while rand not in temp2 and rand not in temp1 and rand not in temp3:
            temp3.append(rand)    
    matrix = [temp1, temp2, temp3]
    return matrix

# get the movement direction from the user
def get_direction():
    move = input("Enter your move: ")
    return move

# swapping of values accordingly when a move is made
def make_a_move(matrix):
    row_idx, col_idx = find_missing_block(matrix)
    valid_moves = find_moves(matrix, row_idx, col_idx)
    moves = []
    for i in valid_moves:
        if(i.find(',')):
            split = i.split(',')
            for i in split:
                moves.append(i)
        else:
            moves.append(i)
    direction = get_direction()
    if direction == 'quit':
        exit()
    while direction in moves:
       matrix = matrix
       if direction == 'up':
            temp = matrix[row_idx+1][col_idx]
            matrix[row_idx][col_idx] = temp
            matrix[row_idx+1][col_idx] = ''

       if direction == 'down':
            temp = matrix[row_idx-1][col_idx]
            matrix[row_idx][col_idx] = temp
            matrix[row_idx-1][col_idx] = ''

       if direction == 'left':
            temp = matrix[row_idx][col_idx+1]
            matrix[row_idx][col_idx] = temp
            matrix[row_idx][col_idx+1] = ''

       if direction == 'right':
            temp = matrix[row_idx][col_idx-1]
            matrix[row_idx][col_idx] = temp
            matrix[row_idx][col_idx-1] = ''

       print_matrix(matrix)
       if(matrix != result_matrix):
            make_a_move(matrix)
       else:
            print("You won")
            input('Press any key to quit')
            exit()
    else:
        print("{} is not a valid move. Enter a valid move.".format(direction))
        make_a_move(matrix)
    print('\n')

# get the possible moves
def find_moves(matrix, row_index, col_index):
    row = ['up', 'up,down', 'down']
    col = ['left', 'left,right', 'right']
    print('Available moves are {},{}'.format(
        row[row_index], col[col_index]))
    print('Enter \'quit\' to exit')
    return [row[row_index], col[col_index]]

# gets the position of block which is emppty
def find_missing_block(matrix):
    for row_idx, row_val in enumerate(matrix):
        for col_idx, col_val in enumerate(row_val):
            if(col_val == ''):
                return row_idx, col_idx


# main program
def main():
    init_matrix = initial_matrix()
    print_matrix(init_matrix)
    make_a_move(init_matrix)

main()


