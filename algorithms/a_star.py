import math
from algorithms.utils import find_min_index

class A_star:
    def __init__(self, grid):
        self.grid = grid

        self.grid.nodes[self.grid.start_node].previous = self.grid.start_node
        self.grid.nodes[self.grid.start_node].distance = 0 + self.heuristic(self.grid.start_node)

        self.grid.nodes[self.grid.start_node].is_active = True
        self.grid.nodes[self.grid.end_node].is_active = True

        self.g_score = {}
        self.g_score[grid.start_node] = 0

    # Diagonal Distance
    def heuristic(self, current_node_index):
        D = 10; D2 = 1.5*14
        current_node_x, current_node_y = self.grid.node_id_to_coordinates(current_node_index)
        end_node_x, end_node_y = self.grid.node_id_to_coordinates(self.grid.end_node)

        dx = abs(current_node_x-end_node_x)
        dy = abs(current_node_y-end_node_y)

        return D*(dx+dy)+(D2-2*D)*min(dx, dy)

    def iter(self):
        min_index = find_min_index(self.grid)

        if min_index == None or self.grid.nodes[self.grid.end_node].visited == True:
            return False

        for (neighbour_index, wt) in self.grid.graph[min_index]:
            if self.grid.nodes[neighbour_index].distance > self.grid.nodes[min_index].distance + wt:
                self.grid.nodes[neighbour_index].previous = min_index

                self.g_score[neighbour_index] = self.g_score[min_index] + wt
                f_score = self.g_score[neighbour_index] + self.heuristic(neighbour_index)

                self.grid.nodes[neighbour_index].distance = f_score 
                self.grid.nodes[neighbour_index].visited = False # Adding neighbour node back to the open set
        
        self.grid.nodes[min_index].visited = True
        return True

    def run(self):
        while self.iter():
            pass

        return self.g_score[self.grid.end_node]