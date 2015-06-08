"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    slide_list = []
    merged_list = []
    result_list =[]
    merge = False     
    #Iterate over the line input looking for non-zero entries. 
    #For each non-zero entry, put the value into the next available 
    #entry of the slide_list (starting at position 0), add 0 in the end to match the length of line
    for number in line:
        if number != 0:
            slide_list.append(number)
    while len(slide_list) != len(line):
        slide_list.append(0)   
    #Iterate over the slide_list and create merged_list 
    #in which pairs of tiles in the slide_list are replaced with 
    #a tile of twice the value and a zero tile.
    for i in range(len(slide_list)-1):
        if slide_list[i] == slide_list[i+1] and merge == False:
            merged_list.append(slide_list[i]*2)
            merged_list.append(0)
            merge = True          
        elif slide_list[i] != slide_list[i+1] and merge == False:
            merged_list.append(slide_list[i])
        else:
            merge = False
    #deal with last element in the list
    if slide_list[-1] != 0 and merge == False:
        merged_list.append(slide_list[-1])
    
    #slide the non-zero to the left
    for number in merged_list:
        if number != 0:
            result_list.append(number)
    while len(result_list) != len(line):
        result_list.append(0)
    return result_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid=[]
        self.reset()
        #list of indices for the initial tiles in the direction.
        #Initial tiles are those whose values appear first in the list 
        #passed to the merge function.
        up_list=[(0,col) for col in range(self.grid_width)]
        down_list=[(self.grid_height-1, col) for col in range(self.grid_width)]
        left_list=[(row, 0) for row in range(self.grid_height)]
        right_list=[(row, self.grid_width-1) for row in range(self.grid_height)]
        self.move_dict={UP:up_list, DOWN:down_list, LEFT:left_list, RIGHT:right_list}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.cell = [[0 for dummy_col in range(self.grid_width)]
                       for dummy_row in range(self.grid_height)]
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.cell)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        new_row = random.randrange(self.grid_height)
        new_col = random.randrange(self.grid_width)
        new_tile = random.choice([2]*90+[4]*10)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.cell[row][col]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.cell[row][col]

#Test
game=TwentyFortyEight(4,5)
game.set_tile(0,3,2)
print game
print game.move_dict


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
