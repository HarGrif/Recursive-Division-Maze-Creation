from maze_class import Maze
import matplotlib.pyplot as plt

maze_size = 25
resolution = 20
gap_size = 1

maze = Maze(maze_size)
maze.draw(resolution, gap_size)

plt.figure()
plt.imshow(maze.grid, cmap='binary')
plt.show()
