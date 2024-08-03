from tkinter import Tk, BOTH, Canvas
from time import sleep

class Window:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def close(self):
        self.is_running = False

    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        

    def draw(self, canvas, fill_color):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cell_center = Point((self.x1 + self.x2) / 2,(self.y1 + self.y2) / 2)
        self._win = win

    def draw(self):
        if self.has_left_wall:
            topleft = Point(self.x1, self.y1)
            bottomleft = Point(self.x1, self.y2)
            line = Line(topleft, bottomleft)
            self._win.draw_line(line, "black")

        if self.has_right_wall:
            topright = Point(self.x2, self.y1)
            bottomright = Point(self.x2, self.y2)
            line = Line(topright, bottomright)
            self._win.draw_line(line, "black")

        if self.has_top_wall:
            topleft = Point(self.x1, self.y1)
            topright = Point(self.x2, self.y1)
            line = Line(topleft, topright)
            self._win.draw_line(line, "black")

        if self.has_bottom_wall:
            bottomleft = Point(self.x1, self.y2)
            bottomright = Point(self.x2, self.y2)
            line = Line(bottomleft, bottomright)
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        line = Line(self.cell_center, to_cell.cell_center)
        
        color = "gray" if undo else "red"
        self._win.draw_line(line, color)




class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1 + j * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                new_cell = Cell(x1, y1, x2, y2, self._win)
                column.append(new_cell)
                self._draw_cell(new_cell)
            self._cells.append(column)
    
    def _draw_cell(self, cell):
        cell.draw()
        self._animate()  # Ensure _animate is called to visualize each step
    
    def _animate(self):
        self._win.redraw()  # Call the window's redraw method to update the display
        sleep(0.05)  # Pause the execution for 0.05 seconds to keep up with each render frame