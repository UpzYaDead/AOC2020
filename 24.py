from typing import Tuple, Dict, Set

import os



class Tiles:
    def __init__(self) -> None:
        self.colours = {}


    def read_instructions(self) -> None:
        mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
        myfile = 'data_24'
        data_24 = os.path.join(mydir, myfile)
        f = open(data_24, "r")
        while True:
            line = f.readline().strip()
            if not line:
                break
            #do some smart parsing
            self.instruction = {'w': 0, 'e' : 0, 'nw': 0, 'se': 0, 'ne': 0,'sw': 0}
            i = 0
            while i < len(line):
                if line[i] != 'w' and line[i] != 'e':
                    instruction = line[i:i+2]
                    self.instruction[instruction] += 1
                    i += 2
                else:
                    self.instruction[line[i]] += 1
                    i += 1
            self.cancel_instruction()
            self.change_tile(self.get_coordinates())


    def cancel_instruction(self):
        # recall
        # w cancels e
        # nw cancels se
        # ne cancels sw

        #w and e
        if self.instruction['w'] > self.instruction['e']:
            #we moved more west than east
            self.instruction['w'] -= self.instruction['e']
            self.instruction['e'] = 0
        else:
            #we moved more east than west
            self.instruction['e'] -= self.instruction['w']
            self.instruction['w'] = 0

        #nw and se
        if self.instruction['nw'] > self.instruction['se']:
            #we moved more west than east
            self.instruction['nw'] -= self.instruction['se']
            self.instruction['se'] = 0
        else:
            #we moved more south east than norht west
            self.instruction['se'] -= self.instruction['nw']
            self.instruction['nw'] = 0

        #ne and sw
        if self.instruction['ne'] > self.instruction['sw']:
            #we moved more north east than south west
            self.instruction['ne'] -= self.instruction['sw']
            self.instruction['sw'] = 0
        else:
            #we moved more south west than north east
            self.instruction['sw'] -= self.instruction['ne']
            self.instruction['ne'] = 0

    def get_coordinates(self) -> Tuple[int, int]:
        first, second = 0, 0
        # e and w
        first += self.instruction['e']
        first -= self.instruction['w']
        #nw and se
        #nw
        first -= self.instruction['nw']
        second += self.instruction['nw']
        #se
        first += self.instruction['se']
        second -= self.instruction['se']
        #sw and ne
        second += self.instruction['ne']
        second -= self.instruction['sw']

        return (first, second)

    def change_tile(self, position: Tuple[int, int]) -> None:
        if position not in self.colours.keys():
            self.colours[position] = 1
        else:
            self.colours[position] += 1

    def number_black_tiles(self) -> int:
        total = 0
        for position in self.colours.keys():
            colour = self.colours.get(position)
            if (colour % 2) != 0:
                total += 1

        return total

    def find_all_neighbours(self):
        neighbours = [
            [1,0],
            [-1,0],
            [1,-1],
            [0,1],
            [0,-1],
            [-1,1]
                     ]
        all_neighbours = set()
        copy_dict = dict(self.colours)
        for coordinate in copy_dict.keys():
            for neighbour in neighbours:
                neigh = [sum(x) for x in zip(coordinate, neighbour)]
                all_neighbours.add(tuple(neigh))

        return all_neighbours

    def greedy_neighbours(self):
        """
        Get all the combinations between (-50,50) and (50,50)
        as starting coordinates.
        """
        coor = set()

        for x in range(-40, 40):
            for y in range(-40, 40):
                coor.add((x,y))
                if (x,y) not in self.colours.keys():
                    print(f"We add {(x,y)}")
                    self.colours[(x,y)] = 0
        return coor

    def change_tiles(self, days: int = 100) -> None:
        neighbours = [
            [1,0],
            [-1,0],
            [1,-1],
            [0,1],
            [0,-1],
            [-1,1]
                     ]
        change_tiles: Dict[Tuple[int, int], bool] = {}
        all_neighbours = self.greedy_neighbours()
        self.find_all_neighbours()
        for _ in range(days):
            print(f"loop {_} {self.number_black_tiles()}")
            if _ >= 1:
                all_neighbours = self.find_all_neighbours()
            for coordinate in all_neighbours:
                if coordinate in self.colours.keys():
                    tile_colour = self.colours.get(coordinate)
                else:
                    self.colours[coordinate] = 0
                    tile_colour = 0
                number_black_tiles = 0
                # print(f"\ncurrent tile {coordinate} colour {self.colours[coordinate]}")
                for neighbour in neighbours:
                    neigh = tuple([sum(x) for x in zip(coordinate, neighbour)])
                    if self.colours.get(neigh) is None:
                        self.colours[neigh] = 0
                    # print(f"neighbour {neigh} colour {self.colours[neigh]}")
                    if tuple(neigh) in self.colours.keys() and (self.colours[neigh] % 2) != 0:
                        number_black_tiles += 1
                if (tile_colour % 2) == 0:
                    #the tile is white
                    if number_black_tiles == 2:
                        # print("we change a white tile to black")
                        change_tiles[coordinate] = True
                    else:
                        change_tiles[coordinate] = False
                else:
                    #the current tile is black
                    if number_black_tiles == 0 or number_black_tiles > 2:
                        # print("We change a black tile to white ")
                        change_tiles[coordinate] = True
                    else:
                        change_tiles[coordinate] = False
            #flip the tiles according to the rules
            for coordinate in all_neighbours:
                if change_tiles[coordinate]:
                    if coordinate not in self.colours.keys():
                        self.colours[coordinate] = 1
                    else:
                        self.colours[coordinate] += 1


tile = Tiles()
tile.read_instructions()
print(tile.colours)
tile.change_tiles(days = 104)
tile.number_black_tiles()

