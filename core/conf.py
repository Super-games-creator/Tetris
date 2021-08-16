V_START = 0.5  # начальная скорость фигуры
V_DOWN = 0.1  # скорость падения фигуры после клавиш Down
BLOCK1 = [(0, 0), (0, 1), (0, 2), (0, 3)]
COLOR1 = "pink"
BLOCK2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
COLOR2 = "lime"
BLOCK3 = [(0, 0), (0, 1), (0, 2), (1, 2)]
COLOR3 = "blue"
BLOCK4 = [(-1, 0), (-1, 1), (0, 0), (0, -1)]
COLOR4 = "red"
BLOCK5 = [(-1, -1), (-1, 0), (0, 0), (0, 1)]
COLOR5 = "orange"
BLOCK6 = [(0, -1), (-1, 0), (0, 0), (0, 1)]
COLOR6 = "yellow"
BLOCK7 = [(0, 0), (0, 1), (0, 2), (-1, 2)]
COLOR7 = "violet"
# кортеж () а список [] отличаются тем что кортеж нельзя менять а список можно
BLOCKS = ((BLOCK1, COLOR1), (BLOCK2, COLOR2), (BLOCK3, COLOR3), (BLOCK4, COLOR4), (BLOCK5, COLOR5),
          (BLOCK6, COLOR6), (BLOCK7, COLOR7))

MX = MY = 1  # внешний отступ
PX = PY = 8  # внутренний отступ
CW = CH = 30
COLS = 12  # число клеток по горизонтали
ROWS = 30  # число клеток по вертикали
W_PANEL = CW * 4
W = COLS*CW + 2*MX+2*PX + W_PANEL
H = ROWS*CH + 2*MY+2*PY
