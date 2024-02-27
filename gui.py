import tkinter as tk
from tkinter import messagebox

# Importing your functions from the provided file
from Cellular_Automata import next_state, Cell
import config


class CellGrid(tk.Canvas):
    def __init__(self, master, cell_size, grid_size, initial_data):
        super().__init__(
            master, width=cell_size * grid_size, height=cell_size * grid_size
        )
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.data = initial_data
        self.rectangles = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        self.draw_grid()

    def draw_grid(self):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                color = self.rgb_to_hex(
                    [self.data[y][x].r, self.data[y][x].g, self.data[y][x].b]
                )
                x0, y0 = x * self.cell_size, y * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                self.rectangles[y][x] = self.create_rectangle(
                    x0, y0, x1, y1, fill=color, outline="gray"
                )

    def update_grid(self, new_data):
        self.data = new_data
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                color = self.rgb_to_hex(self.data[y][x].colour())
                self.itemconfig(self.rectangles[y][x], fill=color)

    def rgb_to_hex(self, rgb):
        return "#{:02x}{:02x}{:02x}".format(*rgb)


def main():
    # Example data: 5x5 grid with random RGB colors
    size = range(config.size)
    state = [[Cell() for x in size] for x in size]
    state[1][1] = Cell(200, 43, 36)
    state[1][2] = Cell(200, 43, 36)
    state[4][11] = Cell(58, 97, 133)
    state[4][13] = Cell(58, 97, 133)
    state[5][12] = Cell(58, 97, 133)

    state[20][1] = Cell(0, 222, 30)
    state[26][1] = Cell(0, 222, 30)
    state[26][2] = Cell(0, 222, 30)
    state[23][1] = Cell(0, 222, 30)
    state[23][2] = Cell(0, 222, 30)
    state[23][4] = Cell(0, 222, 30)

    root = tk.Tk()
    root.title("Cellular Automata GUI")

    cell_size = 10
    grid_size = len(state)

    cell_grid = CellGrid(root, cell_size, grid_size, state)
    cell_grid.pack()

    # Example: Update the grid with new random RGB data
    def update_grid():
        # You should implement the logic to get the new state from your provided functions
        # For demonstration purpose, I'm just updating with random RGB data

        new_state = next_state(cell_grid.data)
        cell_grid.update_grid(new_state)

    # Button to update the grid with new random RGB data
    update_button = tk.Button(root, text="Update Grid", command=update_grid)
    update_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
