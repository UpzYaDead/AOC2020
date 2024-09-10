import os

from typing import List, Union, Tuple

from itertools import product

import math

mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'pepijn_homo'
data_4 = os.path.join(mydir, myfile)
data = []


with open(data_4,'r') as file:
    while (True):
        # read next line
        line = file.readline()
        if not line:
            break
        new_line = line.strip()
        data.append(new_line.split(" "))

def index(lower: int, upper: int, str: str) -> List[Union[int, int]]:
    """
    Front 'F' keeps the lower half of the interval
    Back 'B' keeps the upper half of the interval
    Right 'R' keep upper half
    Left 'L' keep lower half
    """
    if str == 'F': #lower
        return [lower,int(math.floor((upper+lower)/2))]
    elif str == 'B': #upper
        return [int(math.ceil((lower+upper)/2)),upper]
    elif str == 'R': #upper
        return [int(math.ceil((lower+upper)/2)),upper]
    elif str == 'L': #lower
        return [lower, int(math.floor((upper + lower) / 2))]
    else:
        return [-1,-1]

def get_row(str: str, row_range: List[Union[int, int]]) -> int:
    for letter in str:
        lower, upper = row_range[0], row_range[1]
        row_range = index(lower, upper, letter)
    if row_range[0] == row_range[1]:
        return row_range[0]
    else:
        print("The row range is wrong {} ".format(row_range))

def get_column(str: str, col_range: List[Union[int, int]]) -> int:
    for letter in str:
        lower, upper = col_range[0], col_range[1]
        col_range = index(lower, upper, letter)
    if col_range[0] == col_range[1]:
        return col_range[0]
    else:
        print("The row range is wrong {} ".format(col_range))


def boarding_id(str: str) -> int:
    """
    Given the boarding pass, calculate the
    boarding ID.
    """
    row = get_row(str[0:7], [0,127])
    column = get_column(str[7:],[0,7])
    return row * 8 + column

def get_row_col(str: str) -> Tuple[int, int]:
    """
    Given the boarding pass, calculate the
    boarding ID.
    """
    row = get_row(str[0:7], [0,127])
    column = get_column(str[7:],[0,7])
    return (row, column)


#questio 1
# max_id = 0
# for boarding_pass in data:
#     temp = boarding_id(boarding_pass[0])
#     if temp > max_id:
#         max_id = temp
#
# print(max_id)

# rows = [x for x in range(1,127)] #not at the very front or back
# cols = [x for x in range(0,8)] #get all the columns
# all_possible_seats = list(product(rows,cols))

#question2
#so we have to find the missing seat ID. So we'll just go
#over all the ID's and check which one is missing
#get a list of all seat ID's
all_ids = []
for boarding_pass in data:
    id = boarding_id(boarding_pass[0])
    all_ids.append(id)

lowest_id, highest_id = min(all_ids), max(all_ids)

print([x for x in range(lowest_id,highest_id) if x not in all_ids])
print(sorted(all_ids))