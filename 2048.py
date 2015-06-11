"""
Clone of 2048 game.
"""

import poc_2048_gui
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
    merged = False     
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
    for indexi in range(len(slide_list)-1):
        if slide_list[indexi] == slide_list[indexi+1] and merged == False:
            merged_list.append(slide_list[indexi]*2)
            merged_list.append(0)
            merged = True          
        elif slide_list[indexi] != slide_list[indexi+1] and merged == False:
            merged_list.append(slide_list[indexi])
        else:
            merged = False
    #deal with last element in the list
    if slide_list[-1] != 0 and merged == False:
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
        self._height = grid_height
        self._width = grid_width
        self._grid_tile = [[0 for dummy_col in range(self._width)]
                       for dummy_row in range(self._height)]
        #list of indices for the initial tiles in the direction.
        #Initial tiles are those whose values appear first in the list 
        #passed to the merge function.
        up_list=[(0,col) for col in range(self._width)]
        down_list=[(self._height-1, col) for col in range(self._width)]
        left_list=[(row, 0) for row in range(self._height)]
        right_list=[(row, self._width-1) for row in range(self._height)]
        self._move_dict={UP:up_list, DOWN:down_list, LEFT:left_list, RIGHT:right_list}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid_tile = [[0 for dummy_col in range(self._width)]
                       for dummy_row in range(self._height)]
        ##print "creat 1st tile"
        self.new_tile()
        ##print "creat 2nd tile"
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid_tile)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """      
        #Boolean to check if any tile has moved
        changed = False
                
        if direction == UP or direction == DOWN:
            num_steps = self._height
            print "up or down"
        elif direction == LEFT or direction == RIGHT:
            print" left or right"
            num_steps = self._width
        for entry in self._move_dict[direction]:
        #use the direction in the provided OFFSETS dictionary to iterate over 
        #the entries of the associated row or column starting at the specified 
        #initial tile. Retrieve the tile values from those entries, and store 
        #them in a temporary list.   
            temp_list=[]
            pos_list=[]
            for eachstep in range(num_steps):      
                row = entry[0] + eachstep*(OFFSETS[direction])[0]
                col = entry[1] + eachstep*(OFFSETS[direction])[1]
                #function that iterates through the tiles in a grid
                #in a linear direction;
                #entry is a tuple[row,col] denoting the starting tile;
                #Offsets[direction] is a tuple that contains diference btw
                #consecutive tiles in the traversal;
                current_pos=[row, col]
                pos_list.append(current_pos)
                current_tile=self.get_tile(row, col)
                temp_list.append(current_tile)       
            merged_list = merge(temp_list)
            #Use your merge function to merge the tile values in this temporary list
            for index in range(num_steps):
            #store the merged tile values back into the grid
                set_row = pos_list[index][0]
                set_col = pos_list[index][1]
                set_value = merged_list[index]
                ori_value = temp_list[index]
                self.set_tile(set_row, set_col, set_value)
                if set_value != ori_value:
                    changed = True  
            #if any tile has moved, add a new tile to the grid
        if changed == True:
            self.new_tile()
                
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square(tile=0).  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        new_row = random.randrange(self._height)
        new_col = random.randrange(self._width)  
        if self.get_tile(new_row, new_col) == 0:
            new_tile = random.choice([2]*90+[4]*10)
            self.set_tile(new_row, new_col, new_tile)
            return
        else:
            self.new_tile()           
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid_tile[row][col]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid_tile[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))