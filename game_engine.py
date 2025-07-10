import tic_tac_toe_board

while True:
    player_symbol = input("Are you player 'x' or 'o'? ")
    if player_symbol == "x" or player_symbol == "o":
        break
    print("Invalid input. Please try again.")

board = tic_tac_toe_board.TicTacToeBoard(player_turn = player_symbol)

while True:
    print(board.positions)
    
    if board.is_my_turn(player_symbol):
        while True:
            player_move = input("Where would you like to place your marker? ")
            if player_move.isdigit() and int(player_move) in range(9):
                break
            print("Invalid input. Please try again.")
        board.make_move(int(player_move))
    else:
        print("It is not your turn. Please wait.")
    
    print()

    if board.state != "is_playing":
        print(board.positions)
        if board.state == "draw":
            print("The game is a draw!")
        else:
            print(f"Player {board.state} wins!")
        break
    
    print()


