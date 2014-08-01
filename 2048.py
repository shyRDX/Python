"""
Coursera: Principles of Computing Week0 Mini-Project:2048
wiki:https://class.coursera.org/principlescomputing-001/wiki/view?page=2048
codeskulpot:http://www.codeskulptor.org/#user37_AfWQI9m4oD_3.py
Clone of 2048 game.
"""

import poc_2048_gui
import poc_simpletest
#import choice function and use it directly(not random.choice)
from random import choice

#Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

#Offsets for computing tile indices in each direction.
#DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
    DOWN: (-1, 0),
    LEFT: (0, 1),
    RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column 
    in 2048
    """
    dummy_line = [0] * len(line)
    dummy_i = 0
    is_merged = False
    for i in range(len(line)):
        if line[i] != 0:
            if is_merged == False:
                if dummy_line[dummy_i] == line[i]: #merge
                    dummy_line[dummy_i] += line[i]
                    is_merged = True
                    dummy_i += 1
                elif dummy_line[dummy_i] == 0: #start
                    dummy_line[dummy_i] = line[i]
                    is_merged = False
                else: #not equal
                    dummy_line[dummy_i + 1] = line[i]
                    is_merged = False
                    dummy_i += 1
            else: #cannot be merged
                dummy_line[dummy_i] = line[i]
                is_merged = False
    return dummy_line

class TwentyFortyEight(object):
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.grid = [[0 for col in range(grid_width)] \
            for row in range(grid_height)]
        self.reset()
        self.initial_list = {
            UP: [[0, i] for i in range(grid_width)],
            DOWN: [[grid_height-1, i] for i in range(grid_width)],
            LEFT: [[i, 0] for i in range(grid_height)],
            RIGHT: [[i, grid_width-1] for i in range(grid_height)]
            }

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        for dummy_row in range(self.height):
            for dummy_col in range(self.width):
                self.grid[dummy_row][dummy_col] = 0

    def __str__(self):
        """
        Return a string representation of the grid for 
        debugging.
        """
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add a 
        new tile if any tiles moved.
        """
        #get move direction and transform the offset to a list
        move_offset = list(OFFSETS[direction])
        is_moved = False
        #iterate all lines by using initial tiles
        for initial_tile in self.initial_list[direction]:
            #store values to the temp_line
            dummy_row = initial_tile[0]
            dummy_col = initial_tile[1]
            temp_line = []
            temp_index = 0
            while dummy_row in range(self.height) and dummy_col in range(self.width):
                temp_line.append(self.grid[dummy_row][dummy_col])
                dummy_row += move_offset[0]
                dummy_col += move_offset[1]
                temp_index += 1
            #merge the temp_line
            temp_line = merge(temp_line)
            #reset the index for iterating again and assign result values
            dummy_row = initial_tile[0]
            dummy_col = initial_tile[1]
            temp_index = 0
            #iterate again and assign result values
            while dummy_row in range(self.height) and dummy_col in range(self.width):
                is_moved = is_moved or self.grid[dummy_row][dummy_col] != temp_line[temp_index]
                self.grid[dummy_row][dummy_col] = temp_line[temp_index]
                dummy_row += move_offset[0]
                dummy_col += move_offset[1]
                temp_index += 1
        if is_moved:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square. The tile should be 2 90% of the time and 
        4 10% of the time.
        """
        random_value = [2] * 9 + [4]
        zero_squares = []
        for dummy_row in range(self.height):
            for dummy_col in range(self.width):
                if self.grid[dummy_row][dummy_col] == 0:
                    zero_squares.append([dummy_row, dummy_col])
        chosen_value = choice(random_value)
        chosen_square = choice(zero_squares)
        self.grid[chosen_square[0]][chosen_square[1]] = chosen_value

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the
        given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, 
        col.
        """
        return self.grid[row][col]
        
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
