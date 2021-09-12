# check if the game is running
import random

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
                    move_com_with_rnd_smartly()

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


# Computer turn (take random numbers)
def move_com_with_rnd():
    sign = "X"
    done = False
    global is_playing

    while True:
        x = random.randrange(0, 3)
        y = random.randrange(0, 3)

        if not is_game_over(sign):
            if board[x][y] == " " and not done:
                board[x][y] = "X"
                done = True
                print_playground()
                break
            else:
                continue

    if is_game_over(sign):
        is_playing = False
        print("------------GAME  OVER-----------")


# Computer turn (take random numbers in a smart way)
def move_com_with_rnd_smartly():
    sign = "X"
    done = False
    global is_playing

    # set X in board[1][1] to avoid having diagonal attacks if empty
    if board[1][1] == " ":
        board[1][1] = sign
        done = True
        print_playground()

    # Avoid having O in a row (put X when finding 2 X in a row)
    else:
        if not done:

            for i in range(3):
                if board[i][0]=="O" and board[i][2]=="O" and board[i][1] == " ":
                    board[i][1] = sign
                    done = True
                    print_playground()
                    break
                elif board[0][i]=="O" and board[2][i]=="O" and board[1][i] == " ":
                    board[1][i] = sign
                    done = True
                    print_playground()
                    break
                elif board[i][0]=="O" and board[i][1]=="O" and board[i][2] == " ":
                    board[i][2] = sign
                    done = True
                    print_playground()
                    break
                elif board[i][1]=="O" and board[i][2]=="O" and board[i][0] == " ":
                    board[i][0] = sign
                    done = True
                    print_playground()
                    break
                elif board[0][i]=="O" and board[1][i]=="O" and board[2][i] == " ":
                    board[2][i] = sign
                    done = True
                    print_playground()
                    break
                elif board[1][i]=="O" and board[2][i]=="O" and board[0][i] == " ":
                    board[0][i] = sign
                    done = True
                    print_playground()
                    break
                else:
                    continue

            # nobody wins til the field is full
            if is_game_field_full():
                is_playing = False
                print("---------------DRAW-------------")

            if not done:
                while True:
                    x = random.randrange(0, 3)
                    y = random.randrange(0, 3)

                    if not is_game_over(sign):
                        if board[x][y] == " ":
                            board[x][y] = "X"
                            done = True
                            print_playground()
                            break
                        else:
                            continue

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


# check if the game field full is
def is_game_field_full():
    cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                cnt+=1
                continue

    if cnt == 0 or cnt == 1:  # one field is left without any win or zero field is left.
        return True
    return False


print("------Welcome to TicTacToe------")
while is_playing:
    put_coordinates()

