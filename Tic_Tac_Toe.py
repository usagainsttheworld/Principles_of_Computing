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
    
# Add your functions here.
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





