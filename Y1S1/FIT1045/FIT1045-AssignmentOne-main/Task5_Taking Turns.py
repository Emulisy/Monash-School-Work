"""
Task 5: Taking Turns
Task Description
Modify Task 4's code to allow a team of characters to take turns. For this task, we will assume that the team comprises of two characters: Dora and Kirby.

Each character will repeatedly move in one of the four directions until they reach a stopping point value as determined by the user.

You must ensure that each character stay within the boundaries of the board at all times.
"""

import copy

THE_EDGE_OF_INSANITY_1 = [
    ['b', '1', 'b', 'e', 't', 'g', 'e', 'l', '1', '7', 'r', 'u', 's', 'c', 'k', 'f'],
    ['e', 't', 'e', 'b', '2', 'a', '8', 'l', 'y', '2', '4', 'a', 'n', 'd', 'i', 'i'],
    ['g', 'h', 'e', 'g', 'o', 'j', '6', 'd', 'k', 's', 'r', 'i', 'x', 'e', 'u', 'n'],
    ['i', '3', 'l', 'o', 'c', '2', '2', 'e', 'k', '1', '3', '8', 'l', 'j', 'd', 'a'],
    ['n', 'l', 'i', '1', '5', 't', '3', 'n', 't', '8', 'j', 'o', 'e', 'a', '7', 'l']
]

THE_EDGE_OF_INSANITY_2 = [
    ['b', 'o', 's', '4', '8', 'a', 'g', '4', '1', 'e', '7', 'e', '2', 'l', 'o', 'j', 'a', 'a', '3', 'r', 'f'],
    ['e', 'a', 'a', '3', 'r', 'g', 'e', 'c', '9', 'p', 'c', 'y', '6', 'a', 'e', 'k', '5', 'e', 'a', '6', 'i'],
    ['g', '5', 'e', 'a', '6', 'd', 'l', 's', 'h', '5', 'd', 'j', 'l', 'b', 'l', 'u', 'y', 'i', 'k', 'o', 'n'],
    ['i', 'y', 'i', 'k', 'o', '3', 'a', '7', 'k', 'y', 's', 'o', '7', 'r', 'e', 'c', '8', '1', 'p', 'a', 'a'],
    ['n', '8', '1', 'p', 'a', 'r', '1', 'k', 'a', 'e', 'l', 'o', 'a', 'o', '2', 'l', '6', 'b', 'e', 'r', 'l'],
    ['-', '6', 'b', 'e', 'r', 'o', 'n', 'i', '4', 'j', 'k', 'r', 'a', 't', 'n', '8', 'u', 'c', 'g', 'd', '-']
]


# visualise boards
def print_board(board):
    for each_row in board:
        print(" ".join(each_row))


# ask for starting position and replace the position with "*"
def ask_starting_position(board, name, former_char, row_index):
    start_position = (input(f"Choose a starting position for {name} {"(b, e, g, i, n)" if board_select == 1
    else "(b, e, g, i, n, -)"}: "))
    for row in range(len(board)):
        if board[row][0] == start_position:
            board[row][0] = "*"
            row_index = row
            print_board(board)
            former_char = start_position
    return former_char, row_index


# move the "*" towards the input direction
def move(row_index, column_index, former_char, selected_board, name):
    # keep asking for input if the direction is invalid
    while True:
        print()
        print(f"{name}'s current position:")
        print_board(selected_board)
        print()
        direction = input(f"Choose a direction for {name} (u, d, l, r): ")
        former_row = row_index
        former_column = column_index
        reached = False

        # update the index
        if direction == "u":
            row_index -= 1
        elif direction == "d":
            row_index += 1
        elif direction == "l":
            column_index -= 1
        elif direction == "r":
            column_index += 1

        # check if the index is out of range
        if row_index in range(0, len(selected_board)) and column_index in range(0, len(selected_board[row_index])):

            # return the value of former position and store the value of destination, then replace the destination with "*"
            selected_board[former_row][former_column] = former_char
            former_char = selected_board[row_index][column_index]

            # check if the player has reached the destination
            if former_char != stopping_position:
                selected_board[row_index][column_index] = "*"
                print_board(selected_board)
                print(f"{name} has moved!")
                break
            else:
                print(f"{name} reached {stopping_position}!")
                reached = True
                break

        # if current index is invalid, return the value of former index
        else:
            print("Invalid direction. Please try again.")
            row_index = former_row
            column_index = former_column
    return reached, row_index, column_index, former_char


# main body
print()

former_char_Dora = ""
former_char_Kirby = ""
row_index_Dora = 0
column_index_Dora = 0
row_index_Kirby = 0
column_index_Kirby = 0
board_Dora = []
board_Kirby = []
turn = 0

# select board and deep copy to ensure independence of each board
board_select = int(input("Choose a board (1, 2): "))
if board_select == 1:
    board_Dora = copy.deepcopy(THE_EDGE_OF_INSANITY_1)
    board_Kirby = copy.deepcopy(THE_EDGE_OF_INSANITY_1)
    print_board(THE_EDGE_OF_INSANITY_1)
elif board_select == 2:
    board_Dora = copy.deepcopy(THE_EDGE_OF_INSANITY_2)
    board_Kirby = copy.deepcopy(THE_EDGE_OF_INSANITY_2)
    print_board(THE_EDGE_OF_INSANITY_2)

# input stopping position
print()
stopping_position = input("Choose a value for the game's stopping point: \n")

# ask for starting position of each player
former_char_Dora, row_index_Dora = ask_starting_position(board_Dora, "Dora", former_char_Dora, row_index_Dora)
print()
former_char_Kirby, row_index_Kirby = ask_starting_position(board_Kirby, "Kirby", former_char_Kirby, row_index_Kirby)

# take turns to move and stop if one player reached the destination
while True:
    if turn % 2 == 0:
        reached, row_index_Dora, column_index_Dora, former_char_Dora = move(row_index_Dora, column_index_Dora,
                                                                            former_char_Dora, board_Dora, "Dora")
    else:
        reached, row_index_Kirby, column_index_Kirby, former_char_Kirby = move(row_index_Kirby, column_index_Kirby,
                                                                               former_char_Kirby, board_Kirby, "Kirby")
    turn += 1
    if reached:
        break





