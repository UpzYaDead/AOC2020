import os

from typing import Dict, Tuple, List, Union


mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_9'
data_9 = os.path.join(mydir, myfile)
data = []


with open(data_9) as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
        data.append(int(line))
print(data)

def twoSum(data: List[int],target: int) -> bool:
    diff_dict = {}
    for i in range(len(data)):
        diff = target - data[i]
        diff_dict[i] = diff
    # print(diff_dict)
    keys = list(diff_dict.keys())
    vals = list(diff_dict.values())
    for i in range(len(data)):
        val = data[i]
        if val in diff_dict.values():
            index = keys[vals.index(val)]
            print("{} +  {} = {} ".format(val,data[index],val+data[index]))
            print("Indeces {} and {}".format(i,index))
            return True
    return False

def preamble_sum(data: List[int], preamble: int) -> int:
    for i in range(len(data)):
        preamble_data = data[i:(i+preamble)]
        target = data[i+preamble]
        if not twoSum(preamble_data,target):
            return target
    return 0


print(preamble_sum(data,25))

weakness = preamble_sum(data,25)

def find_contiguous_set(data: List[int],weakness: int) -> int:
    for i in range(len(data)):
        for j in range(i,len(data)):
            total =sum(data[i:j])
            if total == weakness:
                print(data[i:j])
                temp = data[i:j]
                return min(temp)+max(temp)
            if total > 10*weakness:
                break
    return 0

print(find_contiguous_set(data,weakness))




