from helpers import draw_board, check_turn, check_for_win
import os
import random

spots = {}
for i in range(10):
    spots[i] = f"{i}"

# track turns
start_option = 0
user_turn = None
computer_turn = None
pvp_turn = 0
start = True
playing_with_other_player = False
playing_with_computer = False
previous_turn = -1
game_won = False
playing_with_other = False

while start:
    print(" WELCOME TO TIC TAC TOE ! \n")
    print("\    /  _  \n")
    print(" \  /  | | \n")
    print("  \/   | | \n")
    print("  /\   | | \n")

    print(
        "User please press y if you want to play with a computer and n if you are playing with another player"
    )
    choice = input()
    if choice == "y":
        playing_with_computer = True
        start = False
    elif choice == "n":
        playing_with_other_player = True
        start = False
    else:
        print("please choose another input")

while playing_with_computer:
    if start_option == 0:
        print(
            "User please press y if you want the computer to start first and n if you want to play first."
        )
    choice = input()
    os.system("cls||clear")
    first_piece = "X"
    second_piece = "O"
    start_option += 1
    user_first = False
    p_v_c_turns = 0

    def p_v_c(user_piece, computer_piece, turn, playing_with_computer, p_v_c_turns):
        while playing_with_computer:

            def check_winner(spots):
                if check_for_win(spots):
                    os.system("cls||clear")
                    print(draw_board(spots))
                    if turn == "user_turn":
                        # print user won, end game
                        print("User has won")
                        print("Thanks for playing!")
                        return True
                    elif turn == "computer_turn":
                        # print computer has won end game
                        print("Computer has won")
                        print("Thanks for playing!")
                        return True
                else:
                    return False

            def check_turns(p_v_c_turns):
                if p_v_c_turns > 8 and not check_winner(spots):
                    return True
                return False

            if turn == "user_turn":
                os.system("cls||clear")
                print(draw_board(spots))
                print(f"User's Turn! Please choose a valid numerical spot or q to quit")
                user_choice = input()
                if user_choice == "q":
                    playing_with_computer = False
                elif str.isdigit(user_choice) and int(user_choice) in spots:
                    if not spots[int(user_choice)] in ["X", "O"]:
                        spots[int(user_choice)] = user_piece
                        p_v_c_turns += 1
                        if (check_winner(spots)) or check_turns(p_v_c_turns):
                            playing_with_computer = False
                        else:
                            p_v_c(
                                first_piece,
                                second_piece,
                                "computer_turn",
                                playing_with_computer,
                                p_v_c_turns,
                            )
                else:
                    print("Please choose a valid spot!")
            elif turn == "computer_turn":
                os.system("cls||clear")
                print(f"Computer's turn!")
                computer_choice = random.randint(1, 9)
                if not spots[int(computer_choice)] in ["X", "O"]:
                    spots[int(computer_choice)] = computer_piece
                    p_v_c_turns += 1
                    if (check_winner(spots)) or check_turns(p_v_c_turns):
                        playing_with_computer = False
                    p_v_c(
                        first_piece,
                        second_piece,
                        "user_turn",
                        playing_with_computer,
                        p_v_c_turns,
                    )
                else:
                    p_v_c(
                        first_piece,
                        second_piece,
                        "computer_turn",
                        playing_with_computer,
                        p_v_c_turns,
                    )

    if choice == "y":
        p_v_c(
            first_piece, second_piece, "user_turn", playing_with_computer, p_v_c_turns
        )
    elif choice == "n":
        p_v_c(
            second_piece,
            first_piece,
            "computer_turn",
            playing_with_computer,
            p_v_c_turns,
        )
    else:
        print("User! Please pick a valid choice to start computer-user game")


while playing_with_other_player:
    # reset screen so board is not drawn every turn
    os.system("cls||clear")
    """
    print tic tac toe board -> tell user what turn it is -> take user input
    """
    print(draw_board(spots))
    if previous_turn == pvp_turn:
        print("That is an invalid spot. Please choose another!")
    player_name = pvp_turn % 2 + 1
    print(f"Player {player_name}'s turn: Pick numerical spot or press q to quit")

    previous_turn = pvp_turn
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
        start = True
        playing_with_other_player = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in ["X", "O"]:
            pvp_turn += 1
            spots[int(choice)] = check_turn(pvp_turn)
    """
    during loop check if a player has won i.e. one of the 3 x cases (vertical, horizontal, diagonal win has occurred

    if our turns have exceeded 8 (0 -> 8) i.e turns are 0 indexed, then we know that there is no winner
    """

    if check_for_win(spots):
        playing_with_other_player = False
        playing_with_other = True
    if pvp_turn > 8:
        playing_with_other_player = False

while playing_with_other:
    """
    as we ended outside loop -> print results
    draw resulting board
    """
    os.system("cls||clear")
    print(draw_board(spots))

    # print winner
    if check_for_win(spots):
        print(f"Player {player_name} has won")
    else:
        print(f"Game has ended in a tie! No Winner :(")
    print("Thanks for playing!")
    playing_with_other = False
