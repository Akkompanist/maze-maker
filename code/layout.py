import pygame

class Grid:
    """
    This class represents a grid layout on the screen.
    """

    def __init__(self, resolution, rows, columns, color=(255, 255, 255), line_color=(0, 0, 0), line_width=1, highlighter_color=(0, 0, 0), start_color = (77,107,83), finish_color = (124, 10, 2) ):
        """
        Initializes a new Grid object.

        Args:
            resolution: A tuple representing the screen resolution (width, height).
            rows: The number of rows in the grid.
            columns: The number of columns in the grid.
            color: The background color of the grid (default: white).
            line_color: The color of the grid lines (default: black).
            line_width: The width of the grid lines (default: 1).
        """

        self.resolution = resolution
        self.line_width = line_width

        self.rows = rows
        self.columns = columns

        self.cell_width = resolution[0] // columns
        self.cell_height = resolution[1] // rows
        
        
        self.start_cell = (0, 0)
        self.finish_cell = (columns - 1, rows - 1)

        self.screen_color = color
        self.line_color = line_color
        self.highlighter_color = highlighter_color
        self.start_color = start_color
        self.finish_color = finish_color


        pygame.init()
        self.screen = pygame.display.set_mode(resolution)

    def get_cell_at_mouse_pos(self):
        mouse_pos = pygame.mouse.get_pos()
        row = mouse_pos[1] // self.cell_height
        column = mouse_pos[0] // self.cell_width
        return row, column
    
    def draw_cells(self, highlighted_cell=None):
        """
        Draws the grid on the screen.
        """

        self.screen.fill(self.screen_color)

        for i in range(self.rows + 1):
            pygame.draw.line(
                self.screen,
                self.line_color,
                (0, i * self.cell_height),
                (self.resolution[0], i * self.cell_height),
                self.line_width
            )

        for j in range(self.columns + 1):
            pygame.draw.line(
                self.screen,
                self.line_color,
                (j * self.cell_width, 0),
                (j * self.cell_width, self.resolution[1]),
                self.line_width
            )

        # Draw start/finish cells using pre-calculated rects
        for cell_pos, color in [(self.start_cell, self.start_color), (self.finish_cell, self.finish_color)]:
            if cell_pos: # Retrieve pre-calculated rect
                pygame.draw.rect(
                self.screen,
                color,
                (cell_pos[0] * self.cell_width + 1, cell_pos[1] * self.cell_height + 1, self.cell_width - 1, self.cell_height - 1)
            )

        if highlighted_cell:
            for row, column in highlighted_cell:
                pygame.draw.rect(
                    self.screen,
                    self.highlighter_color, 
                    (column * self.cell_width + 1, row * self.cell_height + 1, self.cell_width - 1, self.cell_height - 1)
                )

        pygame.display.update()

        
    def remember_cell(self):
        row, column = self.get_cell_at_mouse_pos()
        if self.start_cell is None:
            self.start_cell = (column, row)
        else:
            self.finish_cell = (column, row)
        
if __name__ == "__main__":
    resolution = (1000, 900)  # Example resolution
    columns = resolution[0]//20 # by x
    rows = resolution[1]//20 # by y
    grid_color = (200, 200, 200)  # Light gray background
    line_color = (150, 150, 150)  # Darker gray lines
    line_width = 1
    highlighter_color = (0, 0, 0)  # Black highlighter

    grid = Grid(resolution, rows, columns, grid_color, line_color, line_width, highlighter_color)
    grid.draw_cells()

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
