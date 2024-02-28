import numpy as np
from copy import deepcopy


class Maze:
    def __init__(self, map_size):
        self.grid = np.zeros([map_size, map_size])
        self.start = None
        self.goal = None

    def draw(self, resolution):
        gap_size = max(round((1/4) * (len(self.grid)//(round(np.log(resolution)+1)))), 1)

        # Add boarder to map
        self.grid[0, :] = 1
        self.grid[-1, :] = 1
        self.grid[:, 0] = 1
        self.grid[:, -1] = 1

        step = 0
        while step < resolution:
            step += 1
            step2 = 0
            while step2 < 100:
                step2 += 1
                # Pick a ranom spot in the grid
                test_x = np.random.randint(1, self.grid.shape[0] - 1)
                test_y = np.random.randint(1, self.grid.shape[1] - 1)
                
                # Check vertically and horizontally for boundaries
                edges = [[0, 0], [0, 0]] # [[y1, y2], [x1, x2]]
                # Check right
                i = 0
                while self.grid[test_y, test_x + i] == 0:
                    i += 1
                edges[1][1] = test_x + i
                # Check down
                i = 0
                while self.grid[test_y + i, test_x] == 0:
                    i += 1
                edges[0][0] = test_y + i
                # Check left
                i = 0
                while self.grid[test_y, test_x - i] == 0:
                    i += 1
                edges[1][0] = test_x - i + 1
                # Check up
                i = 0
                while self.grid[test_y - i, test_x] == 0:
                    i += 1
                edges[0][1] = test_y - i + 1

                # Check which gap is larger
                if edges[1][1] - edges[1][0] > edges[0][0] - edges[0][1]:
                    vert_wall = True
                else:
                    vert_wall = False

                # Add randomness to wall oreantation
                # if np.random.randint(10) == 0:
                #     vert_wall = not vert_wall

                if vert_wall:
                    # X gap is larger
                    edge1 = edges[0][1]
                    edge2 = edges[0][0]
                    if edges[1][0] + gap_size < edges[1][1] - gap_size:
                        wall_point = np.random.randint(edges[1][0] + gap_size, edges[1][1] - gap_size)
                    else:
                        continue
                else:
                    # Y gap is larger
                    edge1 = edges[1][0]
                    edge2 = edges[1][1]
                    if edges[0][1] + gap_size < edges[0][0] - gap_size:
                        wall_point = np.random.randint(edges[0][1] + gap_size, edges[0][0] - gap_size)
                    else:
                        continue

                # Check if gap is large enough to place wall
                # If not, try again
                if edge2 - edge1 > 3 * gap_size:
                            
                    if vert_wall:
                        # Plot vertical wall
                        self.grid[edges[0][1]:edges[0][0], wall_point] = 1
                        # Add gap to a random side
                        if np.random.randint(2) == 0:
                            self.grid[edges[0][0] - gap_size:edges[0][0], wall_point] = 2
                        else:
                            self.grid[edges[0][1]:edges[0][1] + gap_size, wall_point] = 2
                    else:
                        # Plot horizontal wall
                        self.grid[wall_point, edges[1][0]:edges[1][1] + 1] = 1
                        # Add gap to a random side
                        if np.random.randint(2) == 0:
                            self.grid[wall_point, edges[1][0]:edges[1][0] + gap_size] = 2
                        else:
                            self.grid[wall_point, edges[1][1] - gap_size:edges[1][1]] = 2
                    break
        
        finding = True
        while finding:
            if self.grid[self.start[1], self.start[0]] == 0:
                if self.grid[self.goal[1], self.goal[0]] == 0:
                    # Check start and goal are 3/4 of the map apart
                    if math.dist(self.start, self.goal) >= map_size:
                        finding = False