"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for cell in self._zombie_list:
            yield cell

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for cell in self._human_list:
            yield cell
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [[self._grid_height * self._grid_width for cell in range(self._grid_width)] 
                          for dummy_row in range(self._grid_height)]
        self._boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            for cell in self._zombie_list:
                self._boundary.enqueue(cell)
        elif entity_type == HUMAN:
            for cell in self._human_list:
                self._boundary.enqueue(cell)
        for cell in self._boundary:
            visited.set_full(cell[0],cell[1])
            distance_field[cell[0]][cell[1]] = 0
        while self._boundary.__len__()>0:
            current_cell = self._boundary.dequeue()
            visited.set_full(current_cell[0],current_cell[1])
            neighbor_cell = self.four_neighbors(current_cell[0],current_cell[1])
            for neighbor in neighbor_cell:
                if self.is_empty(neighbor[0],neighbor[1]) and visited.is_empty(neighbor[0],neighbor[1]):
                    visited.set_full(neighbor[0],neighbor[1])
                    self._boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]]+1
        #print distance_field
        return distance_field
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        human_idx = 0
        for cell in self._human_list:
            neighbors = self.eight_neighbors(cell[0],cell[1])
            neighbors.append(cell)
            max_distance = max ([zombie_distance_field[cell[0]][cell[1]] for cell in neighbors if self.is_empty(cell[0], cell[1])])
            max_list = []
            for each_cell in neighbors:
                if zombie_distance_field[each_cell[0]][each_cell[1]] == max_distance and self.is_empty(each_cell[0], each_cell[1]):
                    max_list.append(each_cell)
            move_cell = random.choice(max_list)
            self._human_list[human_idx]= move_cell
            human_idx += 1
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        zombie_idx = 0
        for cell in self._zombie_list:
            neighbors = self.four_neighbors(cell[0],cell[1])
            neighbors.append(cell)
            min_distance = min ([human_distance_field[cell[0]][cell[1]] for cell in neighbors if self.is_empty(cell[0], cell[1])])
            min_list = []
            for each_cell in neighbors:
                if human_distance_field[each_cell[0]][each_cell[1]] == min_distance and self.is_empty(each_cell[0], each_cell[1]):
                    min_list.append(each_cell)
            move_cell = random.choice(min_list)
            self._zombie_list[zombie_idx]= move_cell
            zombie_idx += 1

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Apocalypse(30, 40))



