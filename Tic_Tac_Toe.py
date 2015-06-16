"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 20      # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 3.0   # Score for squares played by the other player
    
def mc_trial(board, player):
    """
    this function play a game starting with the given player by making 
    random moves, alternating between players. The function return 
    when the game is over
    """
    while board.check_win() is None:
        board.move(random.randrange(0,board.get_dim()),random.randrange(0,board.get_dim()),player)
        board.move(random.randrange(0,board.get_dim()),random.randrange(0,board.get_dim()),provided.switch_player(player))
    else:
        return   

def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the 
    same dimensions as the Tic-Tac-Toe board, a board from a 
    completed game, and which player the machine player is. 
    The function score the completed board and update the scores grid.
    """ 
    for dummy_row in range(board.get_dim()):
        for dummy_col in range(board.get_dim()):
            if board.check_win() == player:
                if board.square(dummy_row, dummy_col) == player:
                    scores[dummy_row][dummy_col] += SCORE_CURRENT
                elif board.square(dummy_row, dummy_col) == provided.switch_player(player):
                    scores[dummy_row][dummy_col] -= SCORE_OTHER
            elif board.check_win() == provided.switch_player(player):
                if board.square(dummy_row, dummy_col) == player:
                    scores[dummy_row][dummy_col] -= SCORE_CURRENT
                elif board.square(dummy_row, dummy_col) == provided.switch_player(player):
                    scores[dummy_row][dummy_col] += SCORE_OTHER
    #print scores

def get_best_move(board, scores):
    """
    The function find all of the empty squares with the maximum score and 
    randomly return one of them as a (row, column) tuple. It is an error to 
    call this function with a board that has no empty squares (there is no possible 
    next move), so your function may do whatever it wants in that case. 
    The case where the board is full will not be tested.
    """
    empty_squares = board.get_empty_squares()
    #board.get_empty_squares() return a list of (row, col) tuples for all empty squares
    maxscore_so_far = scores[empty_squares[0][0]][empty_squares[0][1]]
    #to get the score for the first empty square
    square_w_maxscore = [empty_squares[0]]
    for dummy_square in empty_squares:
        if scores[dummy_square[0]][dummy_square[1]] == maxscore_so_far:
            square_w_maxscore.append(dummy_square)
        elif scores[dummy_square[0]][dummy_square[1]] > maxscore_so_far:
            maxscore_so_far = scores[dummy_square[0]][dummy_square[1]]
            square_w_maxscore = []
            square_w_maxscore.append(dummy_square)  
    #print random.choice(square_w_maxscore)
    return random.choice(square_w_maxscore)

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, 
    and the number of trials to run. The function use the Monte Carlo simulation 
    described above to return a move for the machine player in the form 
    of a (row, column) tuple.
    """
    print board.__str__()
    scores = []
    for dummy_row in range(board.get_dim()):
        scores.append([])
        for dummy_col in range(board.get_dim()):
            scores[dummy_row].append(0)
    for dummy_trial in range(trials):
        trial_board = board.clone()
        #create a copy of the original board and do simulation using the same copy each time
        mc_trial(trial_board, player)
        #print trial_board.__str__()
        mc_update_scores(scores, trial_board, player) 
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

#TEST
#print "empty is", provided.EMPTY
#print "player X is", provided.PLAYERX
#print "player O is", provided.PLAYERO
#print "if draw is", provided.DRAW
#current_board = provided.TTTBoard(4,False, None)
#mc_move(current_board, provided.PLAYERX, NTRIALS)

