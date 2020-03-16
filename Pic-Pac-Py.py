# ------------------ Game State

# represent the board
# represent the amount of turns
# Player X's score
# players O's score
# rounds

# ------------------ Global Variables

# current_player
# win =  False

# ------------------ Logic

# greetings_header
    # print statements

# Show_Board function
    # lots of print statements

# show players turn, then ask for the users input function
    # print current_player
    # input ...

# Insert an X or O in that sqaure as a string function
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