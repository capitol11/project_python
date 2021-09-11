
is_playing = True
board = [[" " for x in range(3)] for y in range(3)]
print(board)

for r in range(3):
    print(" ", board[r][0], "|", board[r][1], "|", board[r][2])
    if r!=2:
        print("----|---|----")

# Player
#board[0][0] = "O"

# Player turn
def move_player(x, y):
    str = "O"
    is_player_turn = True
    global is_playing

    while is_player_turn:
        if not is_game_over(str):
            if board[x][y] == " ":
                board[x][y] = str
                print_playground()
                is_player_turn = False
            else:
                print("Input position is already taken. Try again.")
                break
    # to check if game over is.
    if is_game_over(str):
        is_playing = False
        print("Game Over.")
    else:
        move_com()

def print_playground():
    for r in range(3):
        print(" ", board[r][0], "|", board[r][1], "|", board[r][2])
        if r != 2:
            print("----|---|----")

# Computer turn (in a simple way)
def move_com():
    str = "X"
    done = False
    global is_playing

    if not is_game_over(str):
        for x in range(3):
            for y in range(3):
                if board[x][y] == " " and not done:
                    board[x][y] = "X"
                    done = True
                    print_playground()

    if is_game_over(str):
       is_playing = False
       print("Game Over.")


def is_game_over(str):

    for i in range(3):
        if board[i][0] == str and board[i][1] == str and board[i][2] == str:   # -
            return True
        elif board[0][i] == str and board[1][i] == str and board[2][i] == str:  # |
            return True
        elif board[0][0] == str and board[1][1] == str and board[2][2] == str: # \
            return True
        elif board[0][2] == str and board[1][1] == str and board[2][0] == str: # /
            return True
        else:
            return False


while is_playing:
    x = int(input("Please give an x value: "))
    y = int(input("Please give an y value: "))

    if x < 0 or y < 0 or x >= 3 or y >= 3:
        print("x and y have to be in range between 0 and 2.")
    move_player(x, y)








