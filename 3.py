import os

from typing import List

mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_3'
my_test_file = 'data_3_test'
data_3_test = os.path.join(mydir, my_test_file)
data_3 = os.path.join(mydir, myfile)
data = []
test_data = []


with open(data_3,'r') as file:
    while (True):
        # read next line
        line = file.readline()
        # check if line is not null
        if not line:
            break
        # you can access the line
        data.append(line.strip())

with open(data_3_test,'r') as file:
    while (True):
        # read next line
        line = file.readline()
        # check if line is not null
        if not line:
            break
        # you can access the line
        test_data.append(line.strip())

print(test_data)

def is_tree(str: str) -> bool:
    """
    Checks if the given input is a tree
    """
    return (str == '#')

def move_along_forest(data: List[str], right: int, down: int) -> int:
    """
    Counts the number of trees we encounter
    if we take right and down number of steps
    each time.
    A tree is denoted in the data as '#'
    """
    # print("We print the data: " ,data)
    row, col = 0, 0
    number_of_trees = 0
    length = len(data[0]) #the length of each row
    number_of_rows = len(data)
    while row < number_of_rows:
        col = col % length
        position = data[row][col]
        # print("{}\nWe are now at position {}\nrow and col {} {}".format(data[row],position,row,col))
        if is_tree(position):
            # print("We update the number of trees")
            number_of_trees += 1
        row += down
        col += right
        # print("row var {} max_row {} ".format(row, len(data)))
    return number_of_trees

# print(move_along_forest(data,3,1))


positions = [(1,1),(3,1),(5,1),(7,1),(1,2)]
product = 1
for position in positions:
    product *= move_along_forest(data,position[0],position[1])
    # print(move_along_forest(test_data,position[0],position[1]))
print(product)






