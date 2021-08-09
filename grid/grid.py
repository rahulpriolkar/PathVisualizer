import math

class Node:
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = coordinates
        self.is_active = True
        self.visited = False
        self.distance = math.inf
        self.previous = None
        self.is_path_element = False
    
class Grid:
    def __init__(self, rows, cols, start_node, end_node):
        self.n = rows
        self.size = rows*cols
        self.rows, self.cols = (rows, cols)
        self.nodes = self.initialize_nodes()
        self.graph = []
        self.start_node = start_node
        self.end_node = end_node
    
    def initialize_nodes(self):
        nodes = []
        for i in range(self.rows*self.cols):
            nodes.append(Node(i, self.node_id_to_coordinates(i)))
        return nodes

    def node_id_to_coordinates(self, id):
        return (id//self.rows, id%self.cols)   
    
    def coordinates_to_node_id(self, coordinates):
        return coordinates[0]*self.cols + coordinates[1]

    def is_active_grid_node(self, id):
        return self.nodes[id].is_active
    
    # add an edge from node u to node v, if node v is not inactive
    def add_edge(self, graph, u, v, wt):
        if(self.nodes[v].is_active):
            graph[u].append((v, wt))

    # Adjacency list, an edge is represented as (v, wt), where v is the destination node and wt is the weight
    def create_graph(self):        
        graph = []
        for i in range(0, self.rows*self.cols):
            graph.append([])

            # skip if node is inactive
            if(not self.nodes[i].is_active):
                continue

            if i%self.cols != 0:
                self.add_edge(graph, i, i-1, 10)
            
            if i%self.cols != self.cols-1:
                self.add_edge(graph, i, i+1, 10)

            if int(i/self.cols) != 0:
                self.add_edge(graph, i, i-self.cols, 10)
                if i%self.cols != 0:
                    self.add_edge(graph, i, i-self.cols-1, 14)
                if i%self.cols != self.cols-1:
                    self.add_edge(graph, i, i-self.cols+1, 14)

            if int(i/self.cols) != self.rows-1:
                self.add_edge(graph, i, i+self.cols, 10)
                if i%self.cols != 0:
                    self.add_edge(graph, i, i+self.cols-1, 14)
                if i%self.cols != self.cols-1:
                    self.add_edge(graph, i, i+self.cols+1, 14)

        self.graph = graph

    def get_path(self, target_node):
        path = []
        current_node = target_node
        while current_node != self.start_node:
            current_node = self.nodes[current_node].previous
            if current_node == None:
                return None

            path.insert(0, current_node)
        return path
    
    def reset_grid(self):
        self.nodes = self.initialize_nodes()
        self.graph = []

    def print_graph(self):
        for i in range(0, self.rows*self.cols):
            if i%self.cols == 0:
                print()
            
            print(self.graph[i], end=', ')
        print()

if __name__ == "__main__":
    obj = Grid(4, 5)