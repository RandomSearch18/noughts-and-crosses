X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
BOARD_WIDTH = 3
DIRECTIONS = ["left", "right", "up", "down"]

board = []

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

def has_index(list, index):
    if index < 0: return False
    return index < len(list)

def get_row_from_square(square):
    if square < 0 or square > NUM_SQUARES: return None
    
    column = square % BOARD_WIDTH
    start_index = square - column
    end_index = start_index + BOARD_WIDTH

    return board[start_index:end_index], column


def get_neighbour(square, direction, count = 1):
    if direction not in DIRECTIONS: raise f"{direction} is not a valid direction!"
    if square < 0 or square > NUM_SQUARES: return None
    if count == 0: return board[square]

    row, index = get_row_from_square(square)
    
    if direction == "left":
        target_index = square - count
        return row[target_index] if has_index(row, target_index) else None

    if direction == "right":
        target_index = square + count
        return row[target_index] if has_index(row, target_index) else None

    if direction == "up":
        offset = BOARD_WIDTH * count
        if square >= NUM_SQUARES + offset: return None
        return board[square + offset]

    if direction == "down":
        offset = BOARD_WIDTH * count
        if square >= NUM_SQUARES - offset: return None
        return board[square - offset]

def get_winner(board):
    for square in board:
        for dir in DIRECTIONS:
            # Get the squares that are 0, 1, and 2 squares away
            relevant_squares = []
            for i in range(3):
                relevant_squares.append(get_neighbour(square, dir, i))
                
            # Ignore this direction if we hit a board edge
            if None in relevant_squares:
                continue

            # Work out how many squares each player owns
            owned_squares = {X: 0, O: 0}
            for square in relevant_squares:
                if square == X: owned_squares[X] =+ 1
                if square == O: owned_squares[O] =+ 1

            # Check if any player owns all three of the squares
            for [player, count] in enumerate(owned_squares):
                if count == 3: return player

    # It's a tie if there aren't any empty squares yet
    if EMPTY not in board:
        return TIE

    return None

def main():
    global board
    display_instruct()
    computer, human = get_pieces()
    board = new_board()
    display_board(board)

main()

#print("To view your board, please go to https://cdn.shopify.com/s/files/1/2235/4833/files/Noughts_Crosses_Printables_2.png?v=1536848956")