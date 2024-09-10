import os

from typing import List, Dict

mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_4'
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
print(data)

def make_passport(data: List[List[str]]) -> List[Dict[str, str]]:
    """
    Here the data is the entire list made above.
    So the '' are included to indicate a seperation
    between different passports
    """
    all_passports = []
    passport = {}
    for list in data:
        for line in list:
            if line != '':
                line = line.split(":")
                # print(line)
                key = line[0]
                val = line[1]
                passport[key] = val
            else:
                all_passports.append(passport)
                passport = {}
    return all_passports

def is_valid_passport(passport: Dict[str, str]) -> bool:
    required_fields_set = {"byr","iyr","eyr","hgt","hcl","ecl","pid","cid"}
    also_valid = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
    passport_fields = passport.keys()
    intersect = required_fields_set.intersection(passport_fields)
    if intersect == required_fields_set or intersect == also_valid:
        print("The passport {} is correct".format(passport))
        return True
    else:
        print("The passport {} is wrong".format(passport))
        return False

def between(lower: int, upper: int, val: int) -> bool:
    """
    Check if the val is between lower and upper
    """
    return (lower <= val and val <= upper)

def myFunction(s):
    return (''.join(filter(str.isdigit, s)) or None,
            ''.join(filter(str.isalpha, s)) or None)


def height_check(str: str) -> bool:
    splitted = list(map(myFunction, [str]))
    in_cm_else = splitted[0][1]
    height = int(splitted[0][0])
    if in_cm_else is None or height is None:
        return False
    if in_cm_else == 'in':
        if 59 <= height and height <= 76:
            return True
    elif in_cm_else == 'cm':
        if 150 <= height and height <= 193:
            return True
    else:
        return False
import re
def hair_colour_check(str: str) -> bool:
    if re.match("^#",str): #check if we start with a '#'
        digits = re.findall('[0-9]', str)
        letters = re.findall('[a-f]', str)
        if len(digits)+len(letters) == 6:
            return True
    return False

def eye_colour_check(str: str) -> bool:
    all_colours = {"amb","blu","brn","gry","grn","hzl","oth"}
    if str in all_colours:
        return True
    return False

def passport_id_check(str: str) -> bool:
    return (len(str) == 9) and (str.isdigit())

def data_validation(passport: Dict[str, str]) -> bool:
    """
    A check for all the requirements.
    """
    print("\n\nWe are checking the passport {}".format(passport))
    #byr
    byr_val = int(passport['byr'])
    if not between(1920,2002,byr_val):
        print("The byr was incorrect")
        return False
    #iyr
    iyr_val = int(passport['iyr'])
    if not between(2010, 2020, iyr_val):
        print("The iyr was incorrect")
        return False
    #eyr
    eyr_val = int(passport['eyr'])
    if not between(2020, 2030, eyr_val):
        print("The eyr was incorrect")
        return False
    #hgt
    hgt_val = passport['hgt']
    if not height_check(hgt_val):
        print("The hgt was incorrect")
        return False
    #hcl
    hcl_val = passport['hcl']
    if not hair_colour_check(hcl_val):
        print("The hcl was incorrect")
        return False
    #ecl
    ecl_val = passport['ecl']
    if not eye_colour_check(ecl_val):
        print("The ecl was incorrect")
        return False
    #pid
    pid_val = passport['pid']
    if not passport_id_check(pid_val):
        print("The pid was incorrect")
        return False
    return True

all_passports = make_passport(data)
print(all_passports)
count = 0
count_2 = 0
for passport in all_passports:
    print("")
    if is_valid_passport(passport):
        count += 1
        if data_validation(passport):
            count_2 += 1

print(count)
print(count_2)
