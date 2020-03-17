# ------------------ Game State

board = {
    "a1": None, "a2": None, "a3": None,
    "b1": None, "b2": None, "b3": None,
    "c1": None, "c2": None, "c3": None
}

turns = 9

player_x_score = 0
players_0_score = 0

# ------------------ Global Variables

current_players_turn = "x"
win =  False

# ------------------ Logic

def greetings_header():
    print(" ")
    print("----------------------")
    print("Let's play Pic-Pac-Py!")
    print("----------------------")
    print(" ")
    show_board()

def show_board():
    row_1 = "1)    |   |   "
    row_2 = "2)    |   |   "
    row_3 = "3)    |   |   "

    print("    A   B   C ")
    print("  ")
    print(row_1)
    print("   -----------")
    print(row_2)
    print("   -----------")
    print(row_3)
    print(" ")
    show_player_and_input()

def show_player_and_input():
    print(f"*It is player {current_players_turn.upper()}'s turn*")
    print(" ")
    input("Select a spot you would like to insert your character at...: ").lower()
    print(" ")

def insert():
    if input != "a1" or input != "a2" or input != "a3" or input != "b1" or input != "b2" or input != "b3" or input != "c1" or input != "c2" or input != "c3":
        print("Bogus move! try again")
        show_player_and_input()
    # match the input with the board object
    # if there is no match or the spot is taken
        # print
        # run this function again

# check_for_win function
    # have eight if-else statements that check the board for current_player to see if they won
        # if there is a win change the win variable to True
    # if win == True
        # add a point to the current_player's score
        # run check_for_final_win
    # else run the swap_turns function

# Swap turns function
    # if player X's turn == true
        # players X's turn == false
        # player O's turn == true
    # if player O's turn == true
        # player O's turn == false
        # player X's turn == true
    # run show_board function

# check_for_final_win():
    # if player O's score == 2
        # print the final winner
    # if player X's score == 2 
        # print the final winner
    # else
        # run show_board function

# restart_game
    # reset game state
    # run show_board function

greetings_header()