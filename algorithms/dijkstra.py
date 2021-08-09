import math
from algorithms.utils import find_min_index

class Dijkstra:
    def __init__(self, grid):
        self.grid = grid
        self.grid.nodes[self.grid.start_node].previous = self.grid.start_node
        self.grid.nodes[self.grid.start_node].distance = 0

        self.grid.nodes[self.grid.start_node].is_active = True
        self.grid.nodes[self.grid.end_node].is_active = True

    def iter(self):
        min_index = find_min_index(self.grid)

        if min_index == None or self.grid.nodes[self.grid.end_node].visited == True:
            return False
        
        for (neighbour_index, wt) in self.grid.graph[min_index]:
            if self.grid.nodes[neighbour_index].distance > self.grid.nodes[min_index].distance + wt:
                self.grid.nodes[neighbour_index].previous = min_index
                self.grid.nodes[neighbour_index].distance = self.grid.nodes[min_index].distance + wt
        
        self.grid.nodes[min_index].visited = True
        return True

    def run(self): 
        while self.iter():
            pass

        return self.grid.nodes[self.grid.end_node].distance
