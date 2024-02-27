from Cellular_Automata import Cell


def conways_rule(cell, neighbours):
    alive_neighbours = filter_alive(neighbours)

    match len(alive_neighbours):
        case 3:  # enough neighbours, live
            if cell.is_dead:
                colours = average_colour(alive_neighbours)
                return Cell(*colours)
            else:
                return cell
        case 2:  # perfect neighbours, birth
            return cell
        case _:  # too many or not enough neighbours, death
            return Cell()


def test_rule(cell, neighbours):
    alive_neighbours = filter_alive(neighbours)

    match len(alive_neighbours):
        case 0 | 1:  # perfect neighbours, birth
            return cell
        case _:  # enough neighbours, live
            if cell.is_dead:
                colours = average_colour(alive_neighbours)
                return Cell(*colours)
            else:
                return cell


def average_colour(cells):
    r_acc = 0
    g_acc = 0
    b_acc = 0
    for cell in cells:
        r_acc += cell.r
        g_acc += cell.g
        b_acc += cell.b

    r_acc = r_acc // len(cells)
    g_acc = g_acc // len(cells)
    b_acc = b_acc // len(cells)

    return (r_acc, g_acc, b_acc)


def filter_alive(cells):
    return list(filter(lambda c: not c.is_dead, cells))
