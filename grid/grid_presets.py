import random

# Randomized Grid
def preset1(grid, gui):
    grid.reset_grid()

    random_ids = set([])
    while(len(random_ids) < grid.size//2):
        random_id = random.randint(0, grid.size-1)
        random_ids.add(random_id)
    
    for id in random_ids:
        grid.nodes[id].is_active = False
        # gui.render(scene="grid")
