from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

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

print("You have to guess the location of the enemy battleship in a 5x5 grid.")
print("You have four chances to get it right.")

print("Turn 1")
turn = 1
while turn < 5:
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row not in range(6)) or (guess_col not in range(6)):
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
        if turn < 5:
            print("Turn " + str(turn))
        else:
            print("Go commit die.")
            break