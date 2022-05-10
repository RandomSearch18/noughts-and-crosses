X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
BOARD_WIDTH = 3

DIRECTIONS = ["left", "right", "up", "down"]

def display_instruct():
    """display game instructions"""
    print(
    """\
Welcome to the noughts and crosses game.
This will be a showdown between human and machine.

You will make your move by entering a number 0-8. The number
will correspond to a board position as illustrated:
    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

Prepare yourself, Human. The ultimate battle is about to begin.
"""
    )


def ask_yes_no(question):
    """asks a yes no question"""
    response = None 
    while response not in ("y", "n"): 
        response = input(question).lower()
    return response


def ask_number(question, low, high, exclusive=False):
    """ask for a number within a range"""

    if exclusive:
        # Make the range 1 smaller on each end if `exclusive` is set
        low = low + 1
        high = high - 1

    print(low, high)
    
    response = None
    while not response or response < low or response > high:
        raw_response = input(question)
        # Removes the negative sign from the number, then checks if it's numeric
        is_valid_number = raw_response.lstrip('-').isnumeric()
        # Convert the response to an integer if we can, otherwise use None
        response = int(raw_response) if is_valid_number else None
    return response


def get_pieces():
    # Prompts the player for if they want to go first or not
    go_first = ask_yes_no("Do you want to go first? (y/n): ")
    if go_first == "y":
        # Assign X to the human and O to the computer
        print("\nThen take the first move; you will need it.")
        human = X
        computer = O
    else:
        # Assign O to the human and X to the computer
        print("You will regret this: I will go first.")
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
              +  "| "
              + " | ".join([board[j] for j in range(i,i+BOARD_WIDTH)])
              + " |"
             )
    print(spacing + horizontal_rule)

def legal_moves(board):
    """Creates a list of legal moves"""
    # Creates an array to store the legal moves
    moves = []
    # For each of the 9 squares
    for square in range(NUM_SQUARES):
        # Checks if the square is empty
        if board[square] == EMPTY:
            # Adds the square to the list of moves
            moves.append(square)
    return moves

def get_neighbour(square, direction, count = 1):
    if direction not in DIRECTIONS: raise f"{direction} is not a valid direction!"
    if square < 0: return None
    
    if direction == "left":
        if not (square % BOARD_WIDTH):
            # The square is on the left edge of the board
            return None
        return board[square - 1]

    if direction == "right":
        if not (square + 1) % BOARD_WIDTH:
            # The square is on the right edge of the board
            return None
        return board[square + 1]

    if direction == "up":
        if square < BOARD_WIDTH - 1:
            # The square is on the top row of the board
            return None
        return board[square - BOARD_WIDTH]

    if direction == "down":
        if square >= NUM_SQUARES - BOARD_WIDTH:
            # The square is on the bottom row of the board
            return None
        return board[square + BOARD_WIDTH]

def get_winner(board):
    for square in board:
        for dir in DIRECTIONS:
            
    
    #Add a comment
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))
    #Add a comment
    for row in WAYS_TO_WIN:
        #Add a comment
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    #Add a comment
    if EMPTY not in board:
        return TIE
    return None

def main():
    display_instruct()
    computer, human = get_pieces()
    board = new_board()
    display_board(board)

ask_number("Number? ", -3, 10)
main()

#print("To view your board, please go to https://cdn.shopify.com/s/files/1/2235/4833/files/Noughts_Crosses_Printables_2.png?v=1536848956")