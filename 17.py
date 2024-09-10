

from typing import List, Dict, Tuple, Set
import itertools
from collections import Counter

#only save the positions that are active
#i.e. state == "#"

class Point:
    def __init__(self, x: int, y: int, z: int, state: str):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.state: str = state
        #this map might be unnecessary
        self.map: Dict[Tuple[int, int, int], str] = {(self.x, self.y, self.z): self.state}

    def neighbours(self, x, y, z):
        """
        yield all the 26 neighbours
        """
        for dx, dy, dz in itertools.product([-1,0,1],[-1,0,1],[-1,0,1]):
            if dx != 0 or dy != 0 or dz != 0:
                #we yield, so everything is in place
                #we yield the coordinate
                yield (self.x + dx, self.y + dy, self.z + dz)

    def change_state(self):
        if self.state == ".":
            self.state = "#"
        elif self.state == "#":
            self.state = "."
        else:
            raise ValueError("State not defined")




def neighbours(x: int, y: int, z: int) -> Set[Tuple[int, int, int]]:
    """
    yield all the 26 neighbours
    """
    all_neighbours = set()
    for dx, dy, dz in itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]):
        if dx != 0 or dy != 0 or dz != 0:
            all_neighbours.add((x + dx, y + dy, z + dz))
    return all_neighbours


def step(grid: Dict[Tuple[int, int, int], str]) -> Dict[Tuple[int, int, int], str]:
    new_positions = {p for point in grid.keys() for p in neighbours(point[0], point[1], point[1]) if p not in grid.keys()}
    new_grid = {}


    return new_grid

a = """
.#.
..#
###
"""
RAW = """.#.
..#
###"""


def create_grid(input: str) -> Dict[Tuple[int, int, int], str]:
    grid: Dict[Tuple[int, int, int], str] = {}
    lines = input.split("\n")
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            if col == "#":
                grid[(x,y,0)] = col
    return grid


new_grid =  create_grid(RAW)
print(new_grid)


# grid = make_steps(6, new_grid)
# total_active = len([x for x in grid.keys() if x == "#"])
# print(total_active)













