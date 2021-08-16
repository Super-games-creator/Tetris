import random
from .conf import CW, CH, ROWS, COLS, BLOCKS
from .helper import get_x, get_y, rotate_cells


class Figure:
    def __init__(self, canvas, board):  # это конструктор класса
        self.canvas = canvas  # это поле класса
        self.board = board
        self.p = (3, 1)  # позиция фигуры, объединяем в пару (x, y) это кортеж
        self.cells, self.color = random.choice(BLOCKS)  # выбор случайной фигуры
        self.name = "block"

    def respawn(self, cells, color):
        self.hide()
        self.p = (3, 1)
        self.cells = cells
        self.color = color
        self.draw()
        return self.check(self.p)

    def respawn_forecast(self):
        self.hide()
        self.cells, self.color = random.choice(BLOCKS)  # выбор случайной фигуры
        self.draw()

    def draw_cell(self, cx, cy):
        x = get_x(cx)
        y = get_y(cy)
        self.canvas.create_rectangle(x, y, x + CW, y + CH, fill=self.color, tag=self.name)

    def draw(self):  # это метод класса
        px, py = self.p  # распаковка кортежа
        for cx, cy in self.cells:
            self.draw_cell(cx + px, cy + py)

    def hide(self):
        self.canvas.delete(self.name)

    def move(self):
        px, py = self.p  # распаковка кортежа
        np = (px, py + 1)
        if not self.check(np):
            return False
        self.hide()
        self.p = np
        self.draw()
        return True

    def rotate(self):
        cells_new = rotate_cells(self.cells)
        if not self.check(self.p, cells_new):
            return False
        self.hide()
        self.cells = cells_new
        self.draw()
        return True

    def shift(self, dx):
        px, py = self.p  # распаковка кортежа
        np = (px + dx, py)
        if not self.check(np):
            return False
        self.hide()
        self.p = np
        self.draw()
        return True

    def check(self, np, new_cells=None):
        px, py = np  # распаковка кортежа
        for cx, cy in self.cells if new_cells is None else new_cells:
            if not self.check_cell(cx + px, cy + py):
                return False
        return True

    def check_cell(self, cx, cy):
        return (0 <= cx < COLS) and (0 <= cy < ROWS) and not self.board.in_cells(cx, cy)
