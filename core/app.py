import tkinter as tk
import sched
import time
from .conf import W, COLS, H
from .board import Board
from .figure import Figure


class App:
    def __init__(self):
        self.window = tk.Tk()  # названия модуля.имя класса(с большой буквы)
        self.window.title("Tetris color")
        self.canvas = tk.Canvas(self.window, width=W, height=H)
        self.canvas.pack()
        self.time = time
        self.board = Board(self.canvas)  # это создание экземпляра класса
        self.forecast = Figure(self.canvas, self.board)
        self.forecast.name = "forecast"
        self.forecast.p = (COLS + 2, 10)
        self.figure = Figure(self.canvas, self.board)
        self.s = sched.scheduler(time.time, time.sleep)  # название модуля.имя функции(с маленькой буквы)
        self.close = False

    def restart_game(self):
        self.board.reset()
        self.respawn_figure()

    def on_closing(self):
        self.board.restart.set(1)  # это для сброса окна рестарта
        if self.close:
            self.window.quit()
        self.close = True

    def respawn_figure(self):
        cells = self.forecast.cells
        color = self.forecast.color
        self.forecast.respawn_forecast()
        return self.figure.respawn(cells, color)

    def on_time(self):
        if not self.figure.move():
            self.board.copy_cells(self.figure.cells, self.figure.p, self.figure.color)
            self.board.add_score(1)
            cy = self.board.check_full_line()
            if cy >= 0:
                self.board.hide_cells()
                self.board.del_line(cy)
                self.board.shift_down(cy)
                self.board.draw_cells()
                self.board.add_score(COLS)
                # print("full line")
            if not self.respawn_figure():
                self.board.game_over(self.window)
                self.restart_game()

            self.board.fast_down = False
        self.window.update()
        if not self.close:
            self.s.enter(self.board.v(), 1, self.on_time)

    def on_key(self, event):
        if event.keysym == "Right":
            self.figure.shift(1)

        if event.keysym == "Left":
            self.figure.shift(-1)

        if event.keysym == "Down":
            self.board.fast_down = not self.board.fast_down

        if event.keysym == "Up":
            self.figure.rotate()

    def run(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.bind('<Key>', self.on_key)
        self.board.draw()  # вызов метода класса через точку
        self.board.draw_score()
        self.board.draw_level()
        self.figure.draw()
        self.forecast.draw()
        # window.mainloop()
        self.s.enter(self.board.v(), 1, self.on_time)
        self.s.run()
