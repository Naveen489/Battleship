from random import randint

while True:

    print("BattleShipV2")
    print("1. Play")
    print("2. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        grid = int(input("What size grid do you want?: "))
        attempts = int(input("How many attempts do you need to guess the location of the ship?: "))

        board = []

        for x in range(grid):
            board.append(["O"] * grid)

        def print_board(board):
            for row in board:
                print(" ".join(row))

        print_board(board)

        def random_row(board):
            return randint(0, len(board) - 1)

        def random_col(board):
            return randint(0, len(board[0]) - 1)

        ship_row = random_row(board)
        ship_col = random_col(board)

        print("You have to guess the location of the enemy battleship in the grid.")
        print("You only have a limited number of chances to get it right.")

        print("Turn 1")
        turn = 1
        while turn < attempts + 1:
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))

            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk my battleship!")
                break
            else:
                if (guess_row not in range(grid + 1)) or (guess_col not in range(grid + 1)):
                    print("Outta the damn ocean")
                    print("Turn " + str(turn))
                elif(board[guess_row - 1][guess_col - 1] == "X"):
                    print("Seriously? Again?")
                    print("Turn " + str(turn))
                else:
                    board[guess_row - 1][guess_col - 1] = "X"
                    print("Very sed times, that's a miss")
                    print_board(board)
                    turn += 1
                    if turn < attempts:
                        print("Turn " + str(turn))
                    elif turn > attempts:
                        print("Go commit die.")

    if choice == 2:
        quit("GG boi")

    else:
        print("U bed")
