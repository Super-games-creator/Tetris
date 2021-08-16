import tkinter as tk
from .conf import CW, CH, MX, MY, W_PANEL, W, ROWS, COLS, V_DOWN, H
from .helper import get_x, get_y


class Board:
    def __init__(self, canvas):  # это конструктор класса
        self.canvas = canvas  # это поле класса
        self.cells = []
        self.score = 90
        self.level = 1
        self.fast_down = False
        self.restart = tk.IntVar()  # для рестарта

    def reset(self):
        self.cells = []
        self.score = 0
        self.level = 1
        self.hide_cells()
        self.draw_score()
        self.draw_level()

    def draw_cell(self, cx, cy, color):
        x = get_x(cx)
        y = get_y(cy)
        self.canvas.create_rectangle(x, y, x + CW, y + CH, fill=color, tag="cell")

    def hide_cells(self):
        self.canvas.delete("cell")

    def draw_cells(self):
        for cx, cy, color in self.cells:
            self.draw_cell(cx, cy, color)

    def draw(self):  # это метод класса
        self.canvas.create_rectangle(MX, MY, W - MX - W_PANEL, H - MY, fill="navy", tag="board")

    def draw_score(self):
        self.canvas.delete("score")
        self.canvas.create_text(W - W_PANEL + 5, 60 * MY, text="SCORE:", font=("Arial", 15), anchor="w", tag="score")
        self.canvas.create_text(W - W_PANEL + 5, 90, text=f"{self.score}", font=("Arial", 15), anchor="w", tag="score")

    def draw_level(self):
        self.canvas.delete("level")
        self.canvas.create_text(W - W_PANEL + 5, 130 * MY, text="LEVEL:", font=("Arial", 15), anchor="w", tag="level")
        self.canvas.create_text(W - W_PANEL + 5, 160, text=f"{self.level}", font=("Arial", 15), anchor="w", tag="level")

    def add_score(self, value):
        self.score += value
        if self.score >= 100*self.level:
            self.level += 1
            self.draw_level()
        self.draw_score()

    def copy_cells(self, cells, p, color):
        px, py = p
        for cx, cy in cells:
            self.cells.append((cx + px, cy + py, color))
            self.draw_cell(cx + px, cy + py, color)

    def in_cells(self, cx, cy):
        for fx, fy, color in self.cells:
            if (fx, fy) == (cx, cy):
                return True
        return False

    def check_full_line(self):
        lines = {}  # это словарь
        for fx, fy, color in self.cells:
            lines[fy] = lines[fy] + 1 if fy in lines else 1
        for fy in lines:
            if lines[fy] == COLS:
                return fy
        return -1

    def del_line(self, cy):
        self.cells = list(filter(lambda c: c[1] != cy, self.cells))  # удаления строки cy

    def shift_down(self, cy):  # смещаем вниз строки выше cy
        self.cells = list(map(lambda c: c if c[1] > cy else (c[0], c[1] + 1, c[2]), self.cells))

    def v(self):
        return V_DOWN + 1/(2 + self.level) if not self.fast_down else V_DOWN

    def game_over(self, window):
        self.canvas.create_rectangle(get_x(COLS // 2 - 6), get_y(ROWS // 2 - 6),
                                     get_x(COLS // 2 + 5), get_y(ROWS // 2 + 5), fill="green", tag="game_over")
        self.canvas.create_text(get_x(COLS // 2), get_y(ROWS // 2 - 2),
                                text="!!GAME OVER!!", font=("Arial", 20), fill="red", anchor="c", tag="game_over")
        self.restart.set(0)  # подготовка к рестарту
        button = tk.Button(window, text="RESTART", width=100, height=50, bg="lime", fg="blue", command=self.on_restart)
        button.place(relx=0.39, rely=0.55, anchor="c", width=100, height=50, )
        self.canvas.create_text(get_x(COLS // 2 + -10), get_y(ROWS // 2 + 3),
                                text="SCORE:", font=("Arial", 10), tag="game_over")
        self.canvas.create_text(get_x(COLS // 2 + -7), get_y(ROWS // 2 + 3),
                                text=f"{self.score}", font=("Arial", 10), anchor="w", tag="game_over")
        button.wait_variable(self.restart)  # ждём нажатия на кнопку
        button.destroy()
        self.canvas.delete("game_over")  # сотрём окно рестарта

    def on_restart(self):
        self.restart.set(1)
