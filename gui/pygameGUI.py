import sys
import time
import math
import pygame
from pygame.locals import *
from grid.grid_presets import preset1
from algorithms.dijkstra import Dijkstra
from algorithms.a_star import A_star

class Gui:
    def __init__(self, n, size, grid):
        pygame.init()
        self.n = n
        self.SIZE = size
        self.grid = grid
        self.algorithm = Dijkstra
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.START_COLOR = (219, 35, 192)
        self.END_COLOR = (245, 242, 54)
        self.GRAY = (192, 192, 192)
        self.WHITE = (255, 255, 255)
        self.screen = pygame.display.set_mode(self.SIZE, pygame.RESIZABLE)
        self.cell_size = self.SIZE[0]//self.n
        self.is_mouse_down_left = False
        self.is_mouse_down_right = False
        self.is_ctrl_down = False
        self.is_shift_down = False

    def delay(self, t):
        time.sleep(t)

    def render(self, scene):
        if scene == "menu":
            self.draw_menu()
            self.monitor_input_devices()
        if scene == "grid":
            self.draw_grid()
            self.monitor_input_devices()
    
    def draw_grid(self):
        # grid size params
        grid_size = self.cell_size*self.n

        # Redraw screen to fit nxn grid
        self.screen = pygame.display.set_mode((grid_size, grid_size), pygame.RESIZABLE)
        self.screen.fill(self.WHITE)

        # draw grid
        for i in range(self.n):
            pygame.draw.line(self.screen, self.BLUE, (i*self.cell_size, 0), (i*self.cell_size, self.SIZE[1]))
            pygame.draw.line(self.screen, self.BLUE, (0, i*self.cell_size), (self.SIZE[1], i*self.cell_size)) 

        # color the squares
        for i in range(self.n):
            for j in range(self.n):
                # rectangle adjusted for the thickness of the grid lines
                rect = (j*self.cell_size+1, i*self.cell_size+1, self.cell_size-1, self.cell_size-1) 

                node_id = self.grid.coordinates_to_node_id((i, j))

                color = self.WHITE
                if self.grid.nodes[node_id].distance != math.inf:
                    color = self.RED
                if self.grid.nodes[node_id].visited == True:
                    color = self.GREEN
                if self.grid.nodes[node_id].is_path_element == True:
                    color = self.BLUE
                if self.grid.nodes[node_id].is_active == False:
                    color = self.BLACK
                if self.grid.start_node == node_id:
                    color = self.START_COLOR
                if self.grid.end_node == node_id:
                    color = self.END_COLOR

                pygame.draw.rect(self.screen, color, rect)


        pygame.display.update()
        
    def screen_resize(self, event):
        width, height = event.size
        
        if width > height:
            new_height = min(1080, width)
        else:
            new_height = height
        new_width = new_height

        self.SIZE = (new_width, new_height)
        self.cell_size = self.SIZE[0]//self.n 

        self.screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
    
    def get_node_id(self):
        x, y = pygame.mouse.get_pos()
        return y//self.cell_size * self.n + x//self.cell_size

    def mousebuttondown_handler(self, event):
        if event.button == 1 and self.is_mouse_down_right == False:
            self.is_mouse_down_left = True
        if event.button == 3 and self.is_mouse_down_left == False:
            self.is_mouse_down_right = True

    def mousebuttonup_handler(self, event):
        if event.button == 1 and self.is_mouse_down_right == False:
            self.is_mouse_down_left = False
        if event.button == 3 and self.is_mouse_down_left == False:
            self.is_mouse_down_right = False
    
    def keydown_handler(self, event):
        if event.key == pygame.K_1:
            preset1(self.grid, self)
        if event.key == pygame.K_LCTRL:
            self.is_ctrl_down = True
        if event.key == pygame.K_LSHIFT:
            self.is_shift_down = True
        if event.key == pygame.K_SPACE:
            self.visualize()
        if event.key == pygame.K_ESCAPE:
            self.grid.reset_grid()
        if event.key == pygame.K_a:
            self.algorithm = A_star
        if event.key == pygame.K_d:
            self.algorithm = Dijkstra
            

    def keyup_handler(self, event):
        if event.key == pygame.K_LCTRL:
            self.is_ctrl_down = False
        if event.key == pygame.K_LSHIFT:
            self.is_shift_down = False

    def toggle_node(self):
        if self.is_ctrl_down == False and self.is_shift_down == False and self.is_mouse_down_left == True:
            self.grid.nodes[self.get_node_id()].is_active = False
        if self.is_ctrl_down == False and self.is_shift_down == False and self.is_mouse_down_right == True:
            self.grid.nodes[self.get_node_id()].is_active = True
    
    def mark_node(self):
        if self.is_ctrl_down == True and self.is_shift_down == False and self.is_mouse_down_left == True:
            self.grid.start_node = self.get_node_id()
        if self.is_ctrl_down == False and self.is_shift_down == True and self.is_mouse_down_left == True:
            self.grid.end_node = self.get_node_id()

    def print_path(self, path, color):
        for node_id in path:
            self.grid.nodes[node_id].visited = True
            self.grid.nodes[node_id].is_path_element = True
            self.delay(0.03)

            x, y = self.grid.node_id_to_coordinates(node_id)

            # rectangle adjusted for the thickness of the grid lines
            rect = (y*self.cell_size+1, x*self.cell_size+1, self.cell_size-1, self.cell_size-1) 

            pygame.draw.rect(self.screen, color, rect)
            pygame.display.update()

    def visualize(self):
        self.algo = self.algorithm(self.grid)

        # construct graph from grid
        self.grid.create_graph()

        # run the algorithm
        while self.algo.iter():
            # render the grid after each iteration
            self.delay(0.01)
            self.render(scene="grid") 

        path = self.grid.get_path(self.grid.end_node)
        if path:
            # self.grid.reset_grid() # reset grid
            self.render(scene="grid")
            self.print_path(path, self.BLUE)

    def monitor_input_devices(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                self.screen_resize(event)
            if event.type == MOUSEBUTTONDOWN:
                self.mousebuttondown_handler(event)
            if event.type == MOUSEBUTTONUP :
                self.mousebuttonup_handler(event)
            if event.type == KEYDOWN:
                self.keydown_handler(event)
            if event.type == KEYUP:
                self.keyup_handler(event)

        self.toggle_node()
        self.mark_node()
         
        pygame.display.update()

    def run(self):
        while True:
            self.render(scene="grid")

if __name__ == "__main__":
    gui = Gui(10, (600, 600))
    gui.run()
