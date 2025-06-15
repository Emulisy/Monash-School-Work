"""
Task 4: Navigating Board
Task Description
Modify Task 3's codes to allow the character to take the following actions:

u - move up
d - move down
l - move left
r - move right
The user will repeatedly move the character in one of the four directions until the character reaches a stopping point value.

The character must stay within the boundaries of the board at all times.
"""

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

#visualise boards
def print_board(board):
    for each_row in board:
        print(" ".join(each_row))

print()
board_select=int(input("Choose a board (1, 2): \n"))
stopping_position=input("Choose a value for your stopping point: \n")

former_char=""
row_index=0
column_index=0
selected_board=[]

#select board
if board_select == 1:
    selected_board=THE_EDGE_OF_INSANITY_1
elif board_select == 2:
    selected_board=THE_EDGE_OF_INSANITY_2

start_position=(input(f"Choose a starting position {"(b, e, g, i, n)"if board_select == 1 
                 else"(b, e, g, i, n, -)"}: "))

#replace the selected character with "*" and print the board. Store the former character.
for row in range(len(selected_board)):
    if selected_board[row][column_index] == start_position:
        former_char = selected_board[row][column_index]
        selected_board[row][column_index] = "*"
        row_index = row
        print_board(selected_board)

#keep asking for direction until reaching the stopping position
while former_char != stopping_position:
    print()
    direction=input("Choose a direction (u, d, l, r): ")
    former_row=row_index
    former_column=column_index

    #move and update the index
    if direction == "u":
        row_index-=1
    elif direction == "d":
        row_index+=1
    elif direction == "l":
        column_index-=1
    elif direction == "r":
        column_index+=1

    #check if the index is out of range
    if row_index in range(0, len(selected_board)) and column_index in range(0, len(selected_board[row_index])):
        # return the value of former position and store the value of destination, then replace the destination with "*"
        selected_board[former_row][former_column] = former_char
        former_char = selected_board[row_index][column_index]
        selected_board[row_index][column_index] = "*"
        print_board(selected_board)
    #if current index is invalid, return to the value of former index
    else:
        print("Invalid direction. Please try again.")
        row_index=former_row
        column_index=former_column

print(f"You've reached {stopping_position}!")


