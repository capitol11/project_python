# check if the game is running
is_playing = True

# make game field
board = [[" " for x in range(3)] for y in range(3)]


# player turn
def move_player(x, y):
    sign = "O"
    is_player_turn = True
    global is_playing

    while is_player_turn:
        if not is_game_over(sign):
            if board[x][y] == " ":
                board[x][y] = sign
                print_playground()
                is_player_turn = False

                # to check if game over is.
                if is_game_over(sign):
                    is_playing = False
                    print("------------GAME  OVER-----------")

                else:
                    move_com()

            else:
                print("Input position is already taken. Try again.")
                put_coordinates()


# print gamefield
def print_playground():
    for r in range(3):
        print(" ", board[r][0], "|", board[r][1], "|", board[r][2])
        if r != 2:
            print("----|---|----")
    print("")


# Computer turn (in a simple way)
def move_com():
    sign = "X"
    done = False
    global is_playing

    if not is_game_over(sign):
        for x in range(3):
            for y in range(3):
                if board[x][y] == " " and not done:
                    board[x][y] = "X"
                    done = True
                    print_playground()

    if is_game_over(sign):
        is_playing = False
        print("------------GAME  OVER-----------")


# check game over
def is_game_over(sign):
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:  # -
            return True
        elif board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:  # |
            return True
        elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:  # \
            return True
        elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:  # /
            return True
        else:
            continue
    return False


# get coordinates from console
def put_coordinates():
    try:

        x = int(input("Please give an x value: "))
        y = int(input("Please give an y value: "))
        if x < 0 or y < 0 or x >= 3 or y >= 3:
            raise Exception("x and y have to be in range between 0 and 2.")
        else:
            move_player(x, y)

    except ValueError:
        print("Value error: only number is acceptable.")
    except Exception as e:
        print("Error: ", e)


print("------Welcome to TICTACTOE------")
while is_playing:
    put_coordinates()
