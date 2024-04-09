import pygame 

import maze
import layout

resolution = (1000, 900)  # Example resolution
columns = resolution[0]//20 # by x
rows = resolution[1]//20 # by y

def get_grid():
    
    grid_color = (200, 200, 200)  # Light gray background
    line_color = (150, 150, 150)  # Darker gray lines
    line_width = 1
    highlighter_color = (0, 0, 0)  # Black highlighter

    return layout.Grid(resolution, rows, columns, grid_color, line_color, line_width, highlighter_color)

if __name__ == "__main__":
    grid = get_grid()
    grid.draw_cells()

    maze = maze.Maze(resolution, rows, columns, grid.start_cell, grid.finish_cell)


    running = True
    while running:
        for event in pygame.event.get():
            """Handles mouse click events."""
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                grid.draw_cells([grid.get_cell_at_mouse_pos()])
            
            """ For now start and end will be manual

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                grid.remember_cell()
            """

    pygame.quit()
