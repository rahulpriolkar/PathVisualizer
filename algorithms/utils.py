import math

def find_min_index(grid):
    min_distance = math.inf
    min_index = None
    for i in range(grid.size):
        if min_distance >= grid.nodes[i].distance and grid.nodes[i].visited == False:
            min_distance = grid.nodes[i].distance
            min_index = i
    
    # Rest of the nodes are not reachable
    if min_distance == math.inf:
        min_index = None

    return min_index