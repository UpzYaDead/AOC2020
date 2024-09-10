import os

from typing import List

mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_1'

data_1 = os.path.join(mydir, myfile)
with open(data_1,'r') as file:
    lines = file.readlines()
data = []
for line in lines:
    data.append(int(line[:4]))
print(data)
#part 1
def twoSum(data: List[int],target: int) -> int:
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
            return val*data[index]
    return -1

print(twoSum(data,2020))

# part 2
def threeSum(data,target):
    for i in range(len(data)):
        diff = target-data[i]
        answer = twoSum(data[i:],diff)
        if answer is not None:
            print("elements {}".format(data[i]))
            return answer*data[i]

# print(threeSum(data,2020))