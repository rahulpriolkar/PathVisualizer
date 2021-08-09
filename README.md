# Path Visualizer

## Description
The aim of this project is to allow one to visualize how path finding algorithms work. It consists of a fixed size grid, a start position, a destination position, obstacles and the algorithm.

Currently, two algorithms, Dijkstra's and the A* path finding algorithm have been implemented. Visualizing the two algorithms gives us an insight into how the two algorithms 'think' and how they differ from one another and different scenarios where one might be preferable over the other. A grid preset is also implemented for getting a grid with randomly initialized obstacles. 

The code is modularized such that more algorithms and grid presets can be easily implemented and visualized.

The project is bundled using pyInstaller and any changes to the project will result in a need to rebundle the whole project.

To run the project, simply run the PathVisualizer.exe file.

## Controls
- **A/D** - Select algorithm (A*/Dijkstra)
- **LCTRL + left click** - Select start position
- **LSHIFT + left click** - Select end position
- **left click + (drag)** - Create obstacles
- **right click + (drag)** - Remove obstacles
- **1** - Enable grid preset 1 (Randomized grid)
- **ESC** - Reset screen
- **SPACE** - Visualize path