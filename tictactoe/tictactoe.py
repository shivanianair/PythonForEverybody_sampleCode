"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0

    for rows in board:
        for columns in rows:
            if columns == X:
                x_counter += 1
            elif columns == O:
                o_counter += 1

    if x_counter <= o_counter:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for rows in range(3):
        for columns in range(3):
            if board[rows][columns] == EMPTY:
                moves.add((rows,columns))
    return moves             




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    if board_copy[action[0]][action[1]] != EMPTY:
        raise Exception("Place must be an Not-Played spot")
    else:
        board_copy[action[0]][action[1]] = player(board)

    return board_copy    

    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        #Horizontal matches
        if (board[i][0]==board[i][1]==board[i][2]) and (board[i][0] != EMPTY):
            return board[i][0]
        #Vertical matches    
        if (board[0][i]==board[1][i]==board[2][i]) and (board[0][i] != EMPTY):
            return board[0][i]

    #Diagonal matches
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) \
        and (board[1][1] != EMPTY):
            return board[1][1]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True                


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0    



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        points = -math.inf
        optimal_action = None

        for action in actions(board):
            min_val = minplayer(result(board,action))

            if min_val > points:
                points = min_val
                optimal_action = action

        return optimal_action

    elif player(board) == O:
        points = math.inf
        optimal_action = None

        for action in actions(board):
            min_val = maxplayer(result(board,action))

            if min_val < points:
                points = min_val
                optimal_action = action

        return optimal_action      

def minplayer(board):

    if terminal(board):
        return utility(board)

    num = math.inf

    for action in actions(board):
        num = min(num, maxplayer(result(board,action)))

    return num    
    
def maxplayer(board):

    if terminal(board):
        return utility(board)

    num = -math.inf

    for action in actions(board):
        num = max(num, minplayer(result(board,action)))

    return num

