import os

from typing import Dict, Tuple, List


mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_7'
data_7 = os.path.join(mydir, myfile)
data = []

dict_bags = {}

def construct_data(dict_bag: Dict[str,List[Tuple[int,str]]], line: List[str] ) -> Dict[str,List[Tuple[int,str]]]:
    key = line[0] + " " + line[1]
    for i in range(len(line)):
        if line[i].isdigit():
            val = (int(line[i]),line[i+1] + " " + line[i+2])
            if key in dict_bags.keys():
                dict_bag[key].append(val)
            else:
                dict_bag[key] = [val]
    #a check if the key did not exist, then we set it to None
    if key not in dict_bag.keys():
        dict_bag[key] = [(None,None)]
    return dict_bag

with open(data_7,'r') as file:
    while (True):
        # read next line
        line = file.readline()
        if not line:
            break
        # print(line.split())
        construct_data(dict_bags, line.split())
        # data.append(line.split(" "))

#SOLUTION TO QUESTION 1

# print(dict_bags)
# shiny_bag_set = set()
# old_size = 1
# copy_dict_bags = dict(dict_bags)
#
# #initialization phase
# #add all the elements that map to shiny bags directly, remove them from the dict
# for colour in dict_bags:
#     if colour != "shiny gold":
#         for list in copy_dict_bags[colour]:
#             c_map = list[1]
#             #if this colour maps to the shiny gold bag, we add it to the set and remove it from the dictionary
#             if c_map == "shiny gold":
#                 shiny_bag_set.add(colour)
#                 del copy_dict_bags[colour]
# print("\n\n")
# print(shiny_bag_set)
# print(copy_dict_bags)
#
# all_possible_colours = [key for key in copy_dict_bags.keys()]
#
# print()
# old_size = -1
# while old_size != len(shiny_bag_set):
#     old_size = len(shiny_bag_set)
#     for colour in all_possible_colours:
#         if colour not in shiny_bag_set:
#             #loop over the colours this colour maps to
#             for tuple_list in copy_dict_bags[colour]:
#                 map_colour = tuple_list[1]
#                 if map_colour in shiny_bag_set:
#                     shiny_bag_set.add(colour)
#
# print("\n\nFinal results {} ".format(shiny_bag_set))
# print(len(shiny_bag_set))


#QUESTION 2

def shiny_bag_contains(dict_bags: Dict[str,List[Tuple[int,str]]], colour: str) -> int:
    stack: List[Tuple[int,str]] = [(1,colour)]
    total = 0
    while stack:
        print("\n",stack, "total: ",total )
        multiplier, current_colour = stack.pop()
        print("current: " ,multiplier, current_colour)
        # total += multiplier
        next_colours = dict_bags.get(current_colour)
        print(next_colours)
        for count, child in next_colours:
            if count is not None:
                print(count, child)
                total += count*multiplier
                stack.append((count*multiplier, child))
    return total

print(shiny_bag_contains(dict_bags,"shiny gold"))
