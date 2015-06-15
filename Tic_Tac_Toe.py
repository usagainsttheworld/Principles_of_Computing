"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

def build_scorce_grid(dim):
    score_list = []
    for row in range (dim):
        for col in range(dim):
            element = [row, col, 0]
            score_list.append(element)
    return score_list
    
def mc_trial(board, player):
    """
    this function play a game starting with the given player by making 
    random moves, alternating between players. The function return 
    when the game is over
    """
    while board.check_win() is None:
        board.move(random.randrange(0,3),random.randrange(0,3),player)
        board.move(random.randrange(0,3),random.randrange(0,3),(5-player))
    else:
        return

def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the 
    same dimensions as the Tic-Tac-Toe board, a board from a 
    completed game, and which player the machine player is. 
    The function score the completed board and update the scores grid.
    """ 
    for dummy_square in scores:
        if board.square(dummy_square[0], dummy_square[1]) == board.check_win():        
            dummy_square[2] += 1
        elif board.square(dummy_square[0], dummy_square[1]) == 5-board.check_win():
            dummy_square[2] -= 1  

def get_best_move(board, scores):
    """
    The function find all of the empty squares with the maximum score and 
    randomly return one of them as a (row, column) tuple. It is an error to 
    call this function with a board that has no empty squares (there is no possible 
    next move), so your function may do whatever it wants in that case. 
    The case where the board is full will not be tested.
    """
    highest_so_far = -1
    highest_list = []
    for dummy_square in scores:
        if board.square(dummy_square[0], dummy_square[1]) == 1 and dummy_square[2] >= highest_so_far:
            highest_so_far = dummy_square[2]
            highest_list.append((dummy_square[0], dummy_square[1]))        
    return highest_list          
     
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

print "empty is", provided.EMPTY
print "player X is", provided.PLAYERX
print "player O is", provided.PLAYERO
print "if draw is", provided.DRAW
game = provided.TTTBoard(3,False, None)
print game.get_empty_squares()
print game.__str__()
print "position 0, 0 is", game.square(0,0)
game.move(0,0,provided.PLAYERX)
print game.get_empty_squares()
print "position 0, 0 is", game.square(0,0)
print game.check_win()
print "============="

game = provided.TTTBoard(3,False, None)
mc_trial(game, 2)
print game.__str__()
print "the winner is", game.check_win()
print "============="
game_scorce_grid = build_scorce_grid(3)
print game_scorce_grid
mc_update_scores(game_scorce_grid, game, 2)
print game_scorce_grid
print"============="


game_new = provided.TTTBoard(3,False, None)
print get_best_move(game_new, game_scorce_grid)