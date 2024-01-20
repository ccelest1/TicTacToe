# from main import spots


def draw_board(spots):
    # using dictionary to draw board with f-strings
    # board = "|1|2|3|\n|4|5|6|\n|7|8|9|"
    board = (
        f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
        f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
        f"|{spots[7]}|{spots[8]}|{spots[9]}|"
    )
    return board


"""
we need to make sure the correct player is assigned the correct tic tac toe mark either X or O
- function called in main.py upon a valid integer at an unclaimed spot
"""


def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    return "X"


"""
checking for 'base case' for ending a game
Three in a row: straight vertical, straight horizontal, diagonal
or tie
"""


def check_for_win(spots):
    # horizontal
    if (
        spots[1] == spots[2] == spots[3]
        or spots[4] == spots[5] == spots[6]
        or spots[7] == spots[8] == spots[9]
    ):
        return True
    # vertical
    elif (
        spots[1] == spots[4] == spots[7]
        or spots[2] == spots[5] == spots[8]
        or spots[3] == spots[6] == spots[9]
    ):
        return True
    # diagonal
    elif spots[1] == spots[5] == spots[9] or spots[3] == spots[5] == spots[7]:
        return True
    else:
        return False
