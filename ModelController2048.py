import random

# Win and lose condition global variables
COUNT = 0

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
    output = [0] * len(line)

    index2 = 0
    for index1 in range(len(output)):
        if output[index1] == 0:
            while ((output[index1] == 0) and
                   (index2 < (len(output)))):
                if ((line[index2] != 0) and (index2 >= index1)):
                    output[index1] = line[index2]
                index2 += 1

    for index3 in range(len(output) - 1):
        if ((output[index3] == output[index3 + 1]) and
                (output[index3] != 0)):
            output[index3] += output[index3 + 1]
            output[index3 + 1] = 0

    index2 = 0
    for index1 in range(len(output)):
        if output[index1] == 0:
            while ((output[index1] == 0) and
                   (index2 < (len(output) - 1))):
                index2 += 1
                if ((output[index2] != 0) and (index2 >= index1)):
                    output[index1] = output[index2]
                    output[index2] = 0

    return output


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self.reset()
        self._tile_index = {UP: (0, 0),
                            DOWN: ((self._height - 1), 0),
                            LEFT: (0, 0),
                            RIGHT: (0, (self._width - 1))}

    def reset(self):
        global COUNT
        COUNT = 0

        grid = [[0 for dummy_col in range(self._width)]
                for dummy_row in range(self._height)]

        self._board = grid

        self.new_tile()
        self.new_tile()

    def __str__(self):
        return str(self._board)

    def get_grid_height(self):
        return self._height

    def get_grid_width(self):
        return self._width

    def move(self, direction):
        movement = False
        temporary_row = []

        if (direction == UP) or (direction == DOWN):
            for step_width in range(self._width):
                for step_height in range(self._height):
                    row = self._tile_index[direction][0] + (step_height * OFFSETS[direction][0])
                    col = self._tile_index[direction][1] + (step_width)
                    temporary_row.append(self._board[row][col])

                temporary_row = merge(temporary_row)

                for step_height in range(self._height):
                    row = self._tile_index[direction][0] + (step_height * OFFSETS[direction][0])
                    col = self._tile_index[direction][1] + (step_width)
                    if self._board[row][col] != temporary_row[step_height]:
                        movement = True
                    self._board[row][col] = temporary_row[step_height]

                temporary_row = []

            if movement:
                self.new_tile()

        elif (direction == LEFT) or (direction == RIGHT):
            for step_height in range(self._height):
                for step_width in range(self._width):
                    row = self._tile_index[direction][0] + (step_height)
                    col = self._tile_index[direction][1] + (step_width * OFFSETS[direction][1])
                    temporary_row.append(self._board[row][col])

                temporary_row = merge(temporary_row)

                for step_width in range(self._width):
                    row = self._tile_index[direction][0] + (step_height)
                    col = self._tile_index[direction][1] + (step_width * OFFSETS[direction][1])
                    if self._board[row][col] != temporary_row[step_width]:
                        movement = True
                    self._board[row][col] = temporary_row[step_width]

                temporary_row = []

            if movement:
                self.new_tile()

    def new_tile(self):
        n_tile = random.choice([2] * 9 + [4] * 1)

        zero_tile = False

        while zero_tile == False:
            row = random.choice(range(self._height))
            col = random.choice(range(self._width))

            if self._board[row][col] == 0:
                self._board[row][col] = n_tile
                zero_tile = True
            elif self._board[row][col] != 0:
                zero_tile = False

    def set_tile(self, row, col, value):
        self._board[row][col] = value

    def get_tile(self, row, col):
        return self._board[row][col]

    def win(self):
        global COUNT

        if COUNT == 0:
            for row in range(self._width):
                for col in range(self._height):
                    if self._board[row][col] == 2048:
                        COUNT = 1
                        return True
        return False

    def lose(self):
        not_populated = False

        for row in range(self._width):
            for col in range(self._height):
                if self._board[row][col] == 0:
                    not_populated = True

        if (not_populated == False):
            for row in range(self._width):
                for col in range(self._height - 1):
                    if self._board[row][col] == self._board[row][col + 1]:
                        return False

            for col in range(self._height):
                for row in range(self._width - 1):
                    if self._board[row][col] == self._board[row + 1][col]:
                        return False

            return True