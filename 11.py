RAW = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

puzzle_data = """LL.LL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLL
.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LL.LLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLL.LLLLL.LLLLLLLL
.LLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLL.LLLLLL.LLLLLL.LLLLL..LLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL
L.L.....LL....LLLL....L.L.L...L..L..L.LL.LL.LL.L......L.L..L...L..L.L....LL.......LLL.LL.L.
LLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLL.
LLLLLLLL.LLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLL
LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
.L........LL.L.....L.L..LLLL.LL.L........L...L.L.L......L.........L..LLLLL.......L...LL....
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLL..LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.
LLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LL.LLLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLL.L.LLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.L.LLLLLLL.LLLLLLLL
LLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLLLLL.LLLLLLLLL...LLLLLL
LLLLL.LLLLLL..LLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLL.LLLLLLLLL.LLLL.LLL
.....L.......LL..LL....LLL.LL.LL.L.......LL.L....L.L.L.L.L.L..L......L........L...L..L...L.
LLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.L.LLLLLLL.LLL.LLLL
LLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLL.LLL.LLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLL.LL.LLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL
...L.L...L.L....LL.L.........L.....LLL....L..L..L..L.LLL....L.LL.L.L..L.L..L..LL..L..L..LL.
LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLL.LL.LLLLL
LLLLL.LLLLLLLLLLLLL..LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLL.LLLLLL.LLLL.L..LLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLL..LLLLLLLLLLLLLLLLL
LLLLL.L.LLLL.LLLLLL.LLLLL.LLL.LLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
LLL.L.LLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL
L.LL.L....L....LL.L...LL..........L.......L.LL...LL.LLLLL.....LLL..L.L..L......L..LL..L...L
LLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL
L.LLL.LLLLLL.LLLLLL.LLLLL.LLL.LLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LL.LLLLLLLL
L.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL
..L.LLL.L.L.....L...LL....L......L.L.LL..L..L.L..L....LL........LLL.L.LL.......L...L...L..L
LLLLLLL.LLLL.LL.LLL.LLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLL.LLL.LL.LLLLLL.LLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLL.L.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL
.LLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLL
LLLLL.LLLLLL..LL..LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLL.LLLLLL..LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL.LL.LLLLL
LLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLL.L.LLLL.LLL
.......L.......L.LL...L..L....L.L...L..LL.LLLL.L.L....LLL.L.LL.LL.........LL.L..L...L...L.L
LLLL.LLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.L.LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLL.LL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLL.LL.LLL.LLLLLL.LLLLL.L.LLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
..L...L...LLLLLLLL..L.LL...LL.L.....L.L.....L.....L...L....L.L..........L.L.....L..L..L....
LLLLL.LLLLLL.LLLLLLLLLLLL.L.LLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.
LLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LL.LLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLLLL.LLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL..LLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LL.LLLL.LLLLLLLLL.LLLLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLL.L.LLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
.LL..L.......L...L.L.L......L....L.....L......L........L.L...LLLL...L.L...LLLL.......L.L...
LLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LL.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL..LLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LL.L.LLLLLLLL.LLLLLLL..LLLLLLLLLLLLLLLLL.LLLLLLLL
LL.LL.LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLL.L.LLLLL.LL.LLLLLLL.LLLLLLLLL.LLLLLLL.
LLLLL.LLLLLL.LLLLLL..LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LL.LLLLLL.LLLLLLLL
LLLLL..LLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.L.LLLLLLLLL..LL.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LL
L...L.L..L..L..L...LLL........LLLL.LL..LL.......LLLLL.L.L..L.L.L...L.L.....LL.....LLLL..L..
LLLLL.LLL..LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLL.LL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL..LL.LL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLL.LL.LLLLLLLL
LLLLL.LLLL.L.LLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLL.L.LLLLLL.LLLLLLLLLLL
LLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
LL.LL.LLLLLL.LL.LLL.LLLLLLLLLLL.L.LLLLLLL.LLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLL.LL.LLL.LLLLLL.LLLLL.LLLLLLL.L.LLLLLLLLLL.LLLLLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLL.LLL.LLLLLLL.LLLLLLLLLLLL.LLLLL
....L.L.L......LLL....L..L.L...........L.L......LLL.LL.LL.L.LL.....L.LLLL......L...L.LL.LL.
LLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLL.LL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL
LLLLL.L.LLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLLLLL.LLLLLLLL.LLLLL.LL.LLLLLLL.LL.LLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLL.L.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLL.LLLLLLLLLLLLL.LLLLLLLLLL.LL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLL
LLLLL.LLLLLL.L.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLL.L
....L........L.....LLL....L......LL.L...LLLL.LLL.L.LL.......L.L.L.L......LL..L.LLLL....LL.L
LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLL..LLLLLLLL.LLLLLLLLLLL
LLLLL.LLL.LL.LLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL.LLLLLL.LLLLL.LLL.LL..LLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLL.L.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLL"""

#list of lists structure
from typing import List, Tuple, Dict
from collections import Counter
import os
layout1 = [line for line in RAW.split("\n")]
puzzle_layout = [line for line in puzzle_data.split("\n")]

def neighborhood(layout: List[str],position: Tuple[int,int]) -> Dict[str, int]:
    neighbours = []
    row, col = position

    #row
    #list for indices of the rows
    rows = [(row,col-1),(row,col+1)]
    # print("rows ",rows)
    while rows:
        # print("row loop ",rows)
        try:
            row, col = rows.pop(0)
            if row >= 0 and col >= 0:
                neighbour = layout[row][col]
                # print("The neighbour {} at {} ".format(neighbour,(row,col)))
                neighbours.append(neighbour)
        except:
            pass

    #diagonal
    row, col = position
    diagonals = [(row-1,col-1),(row-1,col+1),(row+1,col-1),(row+1,col+1)]
    # print("diagonals ",diagonals)
    while diagonals:
        try:
            row, col = diagonals.pop(0)
            if row >= 0 and col >= 0:
                neighbour = layout[row][col]
                # print("The neighbour {} at {} ".format(neighbour,(row,col)))

                neighbours.append(neighbour)
        except:
            pass
    #column
    row, col = position
    columns = [(row-1,col),(row+1,col)]
    # print("cols ",columns)
    while columns:
        try:
            row, col = columns.pop(0)
            if row >= 0 and col >= 0:
                neighbour = layout[row][col]
                # print("The neighbour {} at {} ".format(neighbour,(row,col)))

                neighbours.append(neighbour)
        except:
            pass
    # if position == (0, 0):
    #     print("\n\n")
    #     print(neighbours)
    #     print(Counter(neighbours))
    #     for line in prev_layout:
    #         print(line)
    #     print()
    return Counter(neighbours)





def check_adjacent(layout: List[str],position: Tuple[int,int]) -> str:
    """
    From the current position, return the element
    for the updated layout
    """
    row, col = position
    current = layout[row][col]
    neighbours = neighborhood(layout, position)
    if current == "L":
        if "#" not in neighbours.keys():
            return "#"
        else:
            return "L"
    elif current == ".":
        return "."
    elif current == "#":
        if "#" in neighbours.keys():
            if neighbours.get("#") >= 4:
                return "L"
            else:
                return "#"
        else:
            return "#"
    return ""


def create_next(layout: List[str]) -> List[str]:
    new_layout = []
    for row in range(len(layout)):
        cols = layout[row]
        temp = ""
        for col in range(len(cols)):
            temp += (check_adjacent2(layout,(row,col)))
        new_layout.append(temp)
    return new_layout
#
# done = False
# prev_layout = puzzle_layout
# new_layout = None
# while not done:
#     # print("\n\n")
#     # for line in prev_layout:
#     #     print(line)
#     new_layout = create_next(prev_layout)
#     if prev_layout == new_layout:
#         done = True
#     prev_layout = new_layout
# print(new_layout)
# print("\n\n")
# occupied_seats = 0
# for line in new_layout:
#     for seat in line:
#         if seat == "#":
#             occupied_seats+= 1
#
# print(occupied_seats)

#Problem 2
#move into each direction untill we can't no more
# so there has to be some break,


def row_directionn(layout: List[str],position: Tuple[int, int]) -> List[str]:
    """
    Check the status of the first seat in the 2 horizontal directions
    """
    encounters = []
    col_length = len(layout[0])
    init_row, init_col = position
    #right
    col = init_col + 1
    while col < col_length:
        if layout[init_row][col] != '.':
            encounters.append(layout[init_row][col])
            break
        col += 1
    #left
    col = init_col-1
    while col >=0:
        if layout[init_row][col] != '.':
            encounters.append(layout[init_row][col])
            break
        col -= 1
    return encounters


def col_direction(layout: List[str],position: Tuple[int, int]) -> List[str]:
    """
    Check the status of the first seat in the 2 vertical directions
    """
    encounters = []
    row_length = len(layout)
    init_row, init_col = position
    # up
    row = init_row - 1
    while row >= 0:
        if layout[row][init_col] != '.':
            encounters.append(layout[row][init_col])
            break
        row -= 1
    # down
    row = init_row + 1
    while row < row_length:
        if layout[row][init_col] != '.':
            encounters.append(layout[row][init_col])
            break
        row += 1
    return encounters

def diagonal_direction(layout: List[str],position: Tuple[int, int]) -> List[str]:
    """
    Check the status of the first seat in the 4 diagonal direction
    """
    encounters = []
    row_length = len(layout)
    col_length = len(layout[0])
    init_row, init_col = position
    # up-right
    row, col = init_row - 1, init_col + 1
    while row >= 0 and col < col_length:
        if layout[row][col] != '.':
            encounters.append(layout[row][col])
            break
        row -= 1
        col += 1
    #up left
    row, col = init_row - 1, init_col - 1
    while row >= 0 and col >= 0:
        if layout[row][col] != '.':
            if position == (7, 9):
                print("up left We found {} at position {} ".format(layout[row][col],(row,col)))
            encounters.append(layout[row][col])
            break
        row -= 1
        col -= 1
    #down right
    row, col = init_row + 1, init_col + 1
    while row < row_length and col < col_length:
        if layout[row][col] != '.':
            if position == (7, 9):
                print("We found {} at position {} ".format(layout[row][col],(row,col)))
            encounters.append(layout[row][col])
            break
        row += 1
        col += 1
    #down left
    row, col = init_row + 1, init_col - 1
    while row < row_length and col >= 0:
        if layout[row][col] != '.':
            if position == (7, 9):
                print("down left We found {} at position {} ".format(layout[row][col],(row,col)))
            encounters.append(layout[row][col])
            break
        row += 1
        col -= 1
    return encounters


def check_adjacent2(layout: List[str],position: Tuple[int,int]) -> str:
    """
    From the current position, return the element
    for the updated layout
    """
    row, col = position
    current = layout[row][col]
    #TODO: change the neighborhood
    row_neighbors = row_directionn(layout,position)
    col_neighbours = col_direction(layout,position)
    diag_neighbors = diagonal_direction(layout,position)
    directional_neighbours = []
    # directional_neighbours.append(row_neighbors)
    # directional_neighbours.append(col_neighbours)
    # directional_neighbours.append(diag_neighbors)
    for i in row_neighbors:
        directional_neighbours.append(i)
    for j in col_neighbours:
        directional_neighbours.append(j)
    for k in diag_neighbors:
        directional_neighbours.append(k)
    # print("The neighbours: ",directional_neighbours)
    neighbours = Counter(directional_neighbours)
    if position == (7,9):
        print("\nRow neigh {}".format(row_neighbors))
        print("col neigh {}".format(col_neighbours))
        print("diag neigh {}".format(diag_neighbors))
        print(neighbours)

    if current == "L":
        if "#" not in neighbours.keys():
            return "#"
        else:
            return "L"
    elif current == ".":
        return "."
    elif current == "#":
        if "#" in neighbours.keys():
            if neighbours.get("#") >= 5:
                return "L"
            else:
                return "#"
        else:
            return "#"
    return ""

print(layout1)

done = False
prev_layout = puzzle_layout
new_layout = None
while not done:
    print("\n\n")
    for line in prev_layout:
        print(line)
    new_layout = create_next(prev_layout)
    if prev_layout == new_layout:
        done = True
    prev_layout = new_layout
print(new_layout)
print("\n\n")
occupied_seats = 0
for line in new_layout:
    for seat in line:
        if seat == "#":
            occupied_seats+= 1

print("\n haha ",occupied_seats)









