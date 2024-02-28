import numpy as np
from copy import deepcopy


class Maze:
    def __init__(self, map_size):
        self.grid = np.zeros([map_size, map_size])
        self.start = None
        self.goal = None

    def draw(self, resolution, gap_size):
        # Add boarder to map
        self.grid[0, :] = 1
        self.grid[-1, :] = 1
        self.grid[:, 0] = 1
        self.grid[:, -1] = 1

        divis_line_x = []
        divis_line_y = []
        for i in range(1, resolution+1):
            print('\n')
            print("Resolution", i)
            prev_x = 0
            prev_y = 0
            if i % 2 == 0:
                print("Vertical")
                # Steps through x
                for x in range(1, len(self.grid)):
                    # Checks for walls in x
                    checking = True
                    while checking:
                        y_check = np.random.randint(1, len(self.grid)-1)
                        if y_check not in divis_line_y:
                            checking = False

                    if self.grid[y_check, x] != 0 and x - prev_x > gap_size:
                        print("HIT X", x)
                        print(self.grid[1, x])
                        # Steps through y
                        for y in range(1, len(self.grid)):
                            # Checks for walls in y
                            if self.grid[y, 1] != 0 and y - prev_y > gap_size:
                                print("HIT Y", y)
                                print(self.grid[y, 1])

                                # DRAWING THE LINE
                                step = 0
                                drawing = True
                                while drawing:
                                    step += 1
                                    if prev_x+gap_size+1 < x-gap_size-1:
                                        line_x = np.random.randint(prev_x+gap_size+1, x-gap_size-1)
                                        if line_x + 1 not in divis_line_x and line_x - 1 not in divis_line_x:
                                            if y-gap_size-1 > 0 and prev_y+1 < y-gap_size-1:
                                                self.grid[prev_y+1:y, line_x] = 1
                                                gap = np.random.randint(prev_y+1, y-gap_size-1)
                                                self.grid[gap:gap+gap_size, line_x] = 2
                                                drawing = False
                                                divis_line_x.append(line_x)
                                            elif step >= 10:
                                                drawing = False
                                                print("Couldn't draw")
                                        elif step >= 10:
                                            drawing = False
                                            print("Couldn't draw")
                                    elif step >= 10:
                                        drawing = False
                                        print("Couldn't draw")
                                prev_y = deepcopy(y)
            else:
                print("Horizontal")
                # Steps through y
                for y in range(1, len(self.grid)):
                    # Checks for walls in y
                    checking = True
                    while checking:
                        x_check = np.random.randint(1, len(self.grid)-1)
                        if x_check not in divis_line_x:
                            checking = False

                    if self.grid[y, x_check] != 0 and y - prev_y > gap_size:
                        print("HIT Y", y)
                        print(self.grid[y, 1])
                        # Steps through x
                        for x in range(1, len(self.grid)):
                            # Checks for walls in x
                            if self.grid[1, x] != 0 and x - prev_x > gap_size:
                                print("HIT X", x)
                                print(self.grid[1, x])

                                # DRAWING THE LINE
                                drawing = True
                                step = 0
                                while drawing:
                                    step += 1
                                    if prev_y+gap_size+1 < y-gap_size:
                                        line_y = np.random.randint(prev_y+gap_size+1, y-gap_size)
                                        if line_y + 1 not in divis_line_y and line_y - 1 not in divis_line_y:
                                            if x-gap_size-1 > 0 and prev_x+1 < x-gap_size-1:
                                                self.grid[line_y, prev_x+1:x] = 1
                                                gap = np.random.randint(prev_x+1, x-gap_size-1)
                                                self.grid[line_y, gap:gap+gap_size] = 2
                                                drawing = False
                                                divis_line_y.append(line_y)
                                            elif step >= 10:
                                                drawing = False
                                                print("Couldn't draw")
                                        elif step >= 10:
                                            drawing = False
                                            print("Couldn't draw")
                                    elif step >= 10:
                                        drawing = False
                                        print("Couldn't draw")
                                prev_x = deepcopy(x)
