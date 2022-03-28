#noughts and crosses
#demonstartion of functions
#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
BOARD_WIDTH = 3

def display_instruct():
    """display game instructions"""
    print(
    """Welcome to the noughts and crosses game
    this will be a show down between machine and computer

    you will make your move by entering a number 0-8. The number
    will correspond to a board position as illustrated:

        0 | 1 | 2
        3 | 4 | 5
        6 | 7 | 8

    Prepare yourself. Human. The ultimate battle is about to begin. \n"""
    )


def ask_yes_no(question):
    """asks a yes no question"""
    response = None 
    while response not in ("y", "n"): 
        response = input(question.lower())
    return response


def ask_number(question, low, high):
    """ask for a number within a range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    # Prompts the player for if they want to go first or not
    go_first = ask_yes_no("Do you want to go first? (y/n): ")
    if go_first == "y":
        # Assign X to the human and O to the computer
        print("\n Then take the first move you will need it")
        human = X
        computer = O
    else:
        # Assign O to the human and X to the computer
        print("You will regret this: I will go first")
        computer = X
        human = O
    # Returns the symbols for both players
    return computer, human

def new_board():
    """Create a new game board."""
    # Initialises a new array to represent the board
    board = []
    # For each of the 9 squares append(add) it to the board
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    # Return an empty board of 9 squares
    return board


def display_board(board):
    """Display game board on screen."""
    spacing = " " * 4
    horizontal_rule = "+---" * 3 + "+"

    for i in range(0, NUM_SQUARES, BOARD_WIDTH):
        print(spacing + horizontal_rule)
        print(
              spacing
              + "| "
              + " | ".join([board[j] for j in range(i,i+BOARD_WIDTH)])
              + " |"
             )
    print(spacing + horizontal_rule)

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

main()

#print("To view your board, please go to https://cdn.shopify.com/s/files/1/2235/4833/files/Noughts_Crosses_Printables_2.png?v=1536848956")