import tic_tac_toe_board

def main():
    board = tic_tac_toe_board.TicTacToeBoard()
    board.make_move(0)
    board.make_move(1)
    board.make_move(2)
    print(board)


if __name__ == "__main__":
    main()
