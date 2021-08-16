from .conf import CW, CH, MX, MY, PX, PY


def get_x(cx):
    return cx * CW + MX + PX


def get_y(cy):
    return cy * CH + MY + PY


def rotate_cells(cells):
    ax, ay = cells[1]  # а центр вращения

    def get_cell(cx, cy):
        bx, by = cx - ax, cy - ay  # расстояния до центра вращения
        return ax - by, ay + bx

    return [get_cell(cx, cy) for cx, cy in cells]
