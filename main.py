import matplotlib.pyplot as plt
from maze_class import Maze

maze_size = 25
resolution = 4

maze = Maze(maze_size)
maze.draw(resolution)

plt.figure()
plt.imshow(maze.grid, cmap='binary')
plt.show()
