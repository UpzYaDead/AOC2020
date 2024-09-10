import os

from typing import Dict, Tuple, List, Union
from collections import Counter

RAW_1="""16
10
15
5
1
11
7
19
6
12
4"""

RAW_2 = """28
33
18
42
31
14
46
20
48
47
data_24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

jolts_list_1 = sorted([int(x) for x in RAW_1.split("\n")])
jolts_list_2 = sorted([int(x) for x in RAW_2.split("\n")])

mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_10'
data_10 = os.path.join(mydir, myfile)
data = []
jolts_set = set()
with open(data_10, 'r') as file:
    while (True):
        # read next line
        line = file.readline()
        if not line:
            break
        jolts_set.add(int(line))

print(jolts_set)

jolts_list = [0]
while jolts_set:
    min_j = min(jolts_set)
    jolts_set.remove(min_j)
    jolts_list.append(min_j)
print(jolts_list)
jolts_list.append(jolts_list[-1]+3)

def difference_dict(jolts: List[int]) -> Dict[int,int]:
    """
    Return the difference as key to the number
    of times this difference occurs.
    """
    return Counter([jolts[i+1]-jolts[i] for i in range(len(jolts)-1)])

diff_dict = difference_dict(jolts_list)
print(diff_dict)
print(diff_dict[1]*diff_dict[3])

from math import factorial

#question 2

#use dynamic programming, count the # of ways to get to each position.

def number_of_paths(jolts: List[int]) -> int:
    num_ways = [0]*(jolts[-1]+
                    1) #we're not gonna use the 0th index
    #Determine the base cases

    if 1 in jolts:
        num_ways[1] = 1
    if 2 in jolts and 1 in jolts:
        num_ways[2] = 2
    elif 2 in jolts:
        num_ways[2] = 1
    if 3 in jolts and 2 in jolts and 1 in jolts:
        num_ways[3] = 4
    elif 3 in jolts and 2 in jolts:
        num_ways[3] = 2
    elif 3 in jolts and 1 in jolts:
        num_ways[3] = 2
    elif 3 in jolts:
        num_ways[3] = 1

    for i in range(4,max(jolts)+1):
        if i in jolts:
            num_ways[i] = num_ways[i-3]+num_ways[i-2]+num_ways[i-1]

    return num_ways[-1]

print(number_of_paths(jolts_list_1))
print(number_of_paths(jolts_list))











