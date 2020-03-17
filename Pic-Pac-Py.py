# ------------------ Game State

board = {
    "a1": " ", "a2": " ", "a3": " ",
    "b1": " ", "b2": " ", "b3": " ",
    "c1": " ", "c2": " ", "c3": " "
}

turns = 9
score = {"x": 0, "o": 0}
current_players_turn = "x"
win =  False

# ------------------ Logic

def greetings_header():
    print(" ")
    print("----------------------")
    print("Let's play Pic-Pac-Py!")
    print("----------------------")
    print(" ")
    print("Best of 3 wins!")
    show_scores()


def show_scores():
    print(f"X: {score['x']}")
    print(f"O: {score['o']}")
    show_board()


def show_board():
    print(f"""
        a   b   c

    1)  {board["a1"]} | {board["b1"]} | {board["c1"]}
        ----------
    2)  {board["a2"]} | {board["b2"]} | {board["c2"]}
        ----------
    3)  {board["a3"]} | {board["b3"]} | {board["c3"]}
    """)
    print(f"It's player {current_players_turn.upper()}'s turn")
    print(" ")
    input_and_insert()


def input_and_insert():
    global turns
    select = input("Select your spot. e.g 'a1': ")
    print(" ")
    print(" ")
    if select == "a1" or select == "a2" or select == "a3" or select == "b1" or  select == "b2" or select == "b3" or select == "c1" or select == "c2" or select == "c3":
        if board[select] == " ":
            board[select] = current_players_turn
            turns = turns - 1
            check_for_win()
        else:
            print("can not insert on an already occupied cell")
            input_and_insert()
    else:
        print("bogus move! try again") 
        input_and_insert()   


def check_for_win():
    global win, turns, board, current_players_turn
    if board["a1"] == current_players_turn and board["a2"] == current_players_turn and board["a3"] == current_players_turn:
        win = True
        print(f"{current_players_turn} won this round!")
    if board["b1"] == current_players_turn and board["b2"] == current_players_turn and board["b3"] == current_players_turn:
        win = True
        print(f"{current_players_turn} won this round!")
    if board["c1"] == current_players_turn and board["c2"] == current_players_turn and board["c3"] == current_players_turn:
        win = True
        print(f"{current_players_turn} won this round!")
    if board["a1"] == current_players_turn and board["b1"] == current_players_turn and board["c1"] == current_players_turn:
        win = True
        print(f"{current_players_turn} won this round!")
    if board["a2"] == current_players_turn and board["b2"] == current_players_turn and board["c2"] == current_players_turn:
        win = True
        print(f"{current_players_turn} won this round!")
    if board["a3"] == current_players_turn and board["b3"] == current_players_turn and board["c3"] == current_players_turn:
        win = True
        print(f"{current_players_turn} won this round!")
    if board["a1"] == current_players_turn and board["b2"] == current_players_turn and board["c3"] == current_players_turn:
        win = True
        print(f"{current_players_turn} won this round!")
    if board["a3"] == current_players_turn and board["b2"] == current_players_turn and board["c1"] == current_players_turn:
        win = True
        print(f"{current_players_turn} won this round!")
    if win == True:
        if current_players_turn == "x":
            score["x"] = score["x"] + 1
            print(f"A point was added to {current_players_turn}")
        else:
            score["o"] = score["o"] + 1
            print(f"A point was added to {current_players_turn}")
        check_for_final_win()
    elif turns == 0:
        no_winner()
    else: 
        swap_turns()


def no_winner():
    print("no winner and no points added. Restarting game...")
    restart_game()


def swap_turns():
    global current_players_turn
    if current_players_turn == "x":
        current_players_turn = "o"
        show_board()
    if current_players_turn == "o":
        current_players_turn = "x"
        show_board()

def check_for_final_win():
    if score["x"] == 2:
        print("The final winner is X!")
        print("You may continue to play")
        restart_game()
    if score["o"] == 2:
        print("The final winner is O!")
        print("You may continue to play")
        restart_game()
    else:
        restart_game()

def restart_game():
    global board, turns, current_players_turn, win
    board = {
        "a1": " ", "a2": " ", "a3": " ",
        "b1": " ", "b2": " ", "b3": " ",
        "c1": " ", "c2": " ", "c3": " "
    }
    turns = 9
    current_players_turn = "x"
    win =  False
    show_scores()

greetings_header()