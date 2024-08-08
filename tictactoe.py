"""
Tic Tac Toe Player
"""

import math

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
    counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                counter += 1
    if counter % 2 == 0:
        return X
    else: 
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    EmptyStates = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                EmptyStates.append((i,j))
    #for n in EmptyStates:
    #    print(n)
    return EmptyStates

            
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #print(f"Action: {action}")
    if terminal(board):
        return board
    if type(action) != tuple or board[action[0]][action[1]] != EMPTY:
        raise NameError('Invalid Input')
    
    new_board = []
    for x in range(len(board)):
        temp = []
        for elem in board[x]:
            temp.append(elem)
        new_board.append(temp)
        #print(f"Board: {new_board}")

    new_board[action[0]][action[1]] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    elif board [0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
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
    
    if terminal(board):
        return None
    
    current_player = player(board)
    
    def max(board):
        if terminal(board):
            return utility(board) , None
        value = float('-inf') 
        best_move = None
        
        for action in actions(board):
            minVal, _ = min(result(board,action))
            if value < minVal:
                value = minVal
                best_move = action
        return value , best_move
    
    def min(board):
        if terminal(board):
            return utility(board) , None
        value = float('inf') 
        best_move = None
        
        for action in actions(board):
            #print(n , end=" ")
            maxVal, _ = max(result(board,action))
            if value > maxVal:
                value = maxVal
                best_move = action
        return value , best_move
    
    if current_player == X:
        _, action = max(board)
    elif current_player == O:
       _, action = min(board)
       
    return action
    
    
