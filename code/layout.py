import pygame

class Grid:
    """
    This class represents a grid layout on the screen.
    """

    def __init__(self, resolution, rows, columns, color=(255, 255, 255), line_color=(0, 0, 0), line_width=1):
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
        self.rows = rows
        self.columns = columns
        self.cell_width = resolution[0] // columns
        self.cell_height = resolution[1] // rows
        self.color = color
        self.line_color = line_color
        self.line_width = line_width

        pygame.init()
        self.screen = pygame.display.set_mode(resolution)

    def draw(self, update=True):
        """
        Draws the grid on the screen.

        Args:
            update: Whether to update the display after drawing (default: True).
        """

        self.screen.fill(self.color)

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

        if update:
            pygame.display.update()

    def highlight_cell(self, row, column, color = (0, 0, 0)):
        """
        Highlights a specific cell in the grid.

        Args:
            row: The row index of the cell to highlight.
            column: The column index of the cell to highlight.
            color: The color of the highlight. (default: black)
        """

        self.draw(False)  # Clear the previous grid before highlighting

        # Draw highlight rectangle with a slight inset to avoid line overlap
        pygame.draw.rect(
            self.screen,
            color,
            (column * self.cell_width + 1, row * self.cell_height + 1, self.cell_width - 1, self.cell_height - 1)
        )
        
        pygame.display.update()


if __name__ == "__main__":
    resolution = (900, 900)  # Example resolution
    rows = 10
    columns = 10
    grid_color = (200, 200, 200)  # Light gray background
    line_color = (150, 150, 150)  # Darker gray lines
    highlighter_color = (0, 0, 0)  # Black highlighter
    clock = pygame.time.Clock()

    grid = Grid(resolution, rows, columns, grid_color, line_color)
    grid.draw(True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[1] // grid.cell_height
                column = mouse_pos[0] // grid.cell_width
                grid.highlight_cell(row, column, highlighter_color)

        clock.tick(60)  # Limit framerate to 60 FPS

    pygame.quit()
