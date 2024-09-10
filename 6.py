import os

from typing import Set, List


mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_6'
data_6 = os.path.join(mydir, myfile)
data = []

count = 0
def string_to_set(str: str) -> Set[str]:
    s = set()
    for letter in str:
        s.add(letter)
    return s

def add_count(list: List[Set[str]],count: int) -> int:
    print("\n\nThe list:")
    print(list)
    unique_set = set.intersection(*list)
    print(unique_set)
    return count + len(unique_set)




answers =  set()
l = []
with open(data_6,'r') as file:
    while (True):
        # read next line
        line = file.readline()
        if not line:
            count = add_count(l, count)
            break
        new_line = line.strip()
        if new_line == '':
            count = add_count(l,count)
            l = []
        else:
            l.append(string_to_set(new_line))
print(count)