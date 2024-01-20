from helpers import draw_board, check_turn, check_for_win
import os

spots = {}
for i in range(10):
    spots[i] = f"{i}"

# track turns
turn = 0
playing = True
previous_turn = -1
game_won = False

while playing:
    # reset screen so board is not drawn every turn
    os.system("cls||clear")
    """
    print tic tac toe board -> tell user what turn it is -> take user input
    """
    print(draw_board(spots))
    if previous_turn == turn:
        print("That is an invalid spot. Please choose another!")
    player_name = turn % 2 + 1
    print(f"Player {player_name}'s turn: Pick numerical spot or press q to quit")

    previous_turn = turn
    choice = input()

    """
    communicate to player that input was invalid
    """

    """
    first case: if user quits end  game
    second case: check to make sure user enters an input that is an integer between 1 and 9
        sub case: check to make sure spot has not already yet been claimed
    """
    if choice == "q":
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in ["X", "O"]:
            turn += 1
            spots[int(choice)] = check_turn(turn)
    """
    during loop check if a player has won i.e. one of the 3 x cases (vertical, horizontal, diagonal win has occurred

    if our turns have exceeded 8 (0 -> 8) i.e turns are 0 indexed, then we know that there is no winner
    """
    if check_for_win(spots):
        playing = False
        game_won = True
    if turn > 8:
        playing = False

"""
as we ended outside loop -> print results
draw resulting board
"""
os.system("cls||clear")
print(draw_board(spots))

# print winner
if game_won:
    print(f"Player {player_name} has won")
else:
    print(f"Game has ended in a tie! No Winner :(")
print("Thanks for playing!")
