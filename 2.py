import os

from typing import Dict, Tuple, List

mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_2'

data_2 = os.path.join(mydir, myfile)

with open(data_2,'r') as file:
    lines = file.readlines()
data = []

def split_num(str) -> Tuple[int,int]:
    elements = str.split("-")
    return int(elements[0]),int(elements[1])

def count_letter(password: str) -> Dict[str, int]:
    count_dict = {}
    for letter in password:
        if letter != '\n':
            if letter in count_dict.keys():
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
    return count_dict


def check_1(list) -> bool:
    """
    A check for the first question of the second day
    """
    print("\n")
    lower, upper  = split_num(list[0])
    letter, string = list[1][0], list[2][:-1]
    count_dict = count_letter(string)
    try:
        num_appearences = count_dict[letter]
    except:
        num_appearences = 0
    print("The total data {}\nThe letter we want to check {}\nThe dict count {} ".format(list,letter,count_dict))
    if lower <= num_appearences and num_appearences <= upper:
        print("True")
        return True
    else:
        print("False")
        return False


def check_2(list) -> bool:
    """
    A check for the second question of the second day
    """
    print("\n")
    print(list)
    lower, upper = split_num(list[0])
    letter, string = list[1][0], list[2][:-1]
    print(string)
    print("target {} \nposition  {} letter {}, position  {} letter {}".format(letter,lower,string[lower-1],upper,string[upper-1]))
    first = letter == string[lower-1]
    second = letter == string[upper-1]
    if first or second:
        return first ^ second



count_1 = 0
count_2 = 0

for line in lines:
    some = line.split(" ")
    # if check_1(some):
    #     count_1 += 1
    if check_2(some):
        count_2 += 1


print(count_1)
print(count_2)