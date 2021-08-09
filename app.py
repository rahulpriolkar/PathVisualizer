from grid.grid import Grid
from gui.pygameGUI import Gui

if __name__ == "__main__":
    n = 60; star_node = 0; end_node = n**2-1
    grid = Grid(n, n, star_node, end_node)
    
    gui = Gui(n, (800, 800), grid)

    gui.run()