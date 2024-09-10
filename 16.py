RAW = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


#probably a smart way of doing it with regex, but I
# do not really know how to use them.
import os
import re
from typing import Tuple, List, Set

class Field:
    def __init__(self, name: str, lower1: int, upper1: int, lower2: int, upper2: int) -> None:
        self.name = name
        self.range1 = {i for  i in range(lower1, upper1+1)}
        self.range2 = {i for  i in range(lower2, upper2+1)}


    def in_range(self, num: int) -> bool:
        # print("num {} in {}\nor in {}\n{}".format(num, self.range1, self.range2,(num in self.range1 or num in self.range2)))
        return (num in self.range1 or num in self.range2)

class Ticket:
    def __init__(self, fields: List[Field]) -> None:
        self.fields = fields

    def in_range(self, num: int) -> bool:
        for field in self.fields:
            # print("Check for {} in {} or {}".format(num, field.range1, field.range2))
            if field.in_range(num):
                return True
        # print("{} is not in any range".format(num))
        return False

class Possible:
    def __init__(self, ticket: Ticket) -> None:
        self.possible_fields = {field.name for field in ticket.fields}
        self.ticket = ticket

    def check(self, num: int) -> None:
        possible = set()
        for field in self.ticket.fields:
            # print(num in field.range1 or num in field.range2)
            if num in field.range1:
                # print("We add something to a set")
                possible.add(field.name)
            if num in field.range2:
                # print("We add something to a set")
                possible.add(field.name)
        # print("\n--------------------------------------------------------------\nWe intersect possible {} and {} ".format(possible, self.possible_fields))
        self.possible_fields = self.possible_fields.intersection(possible)
        # print("Result ",self.possible_fields)


def create_ticket() -> Ticket:
    mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
    myfile = 'data_16'

    data_16 = os.path.join(mydir, myfile)
    fields: List[Field] = []
    with open(data_16,'r') as file:
        while (True):
            print("\n\n")
            # read next line
            line = file.readline()
            if not line or line == "\n":
                break
            print(line)
            name = line.split(":")[0]
            print(name)
            bounds =  re.findall(r'\b\d+\b', line)
            for i in range(len(bounds)):
                bounds[i] = int(bounds[i])
            print(bounds)
            fields.append(Field(name, bounds[0], bounds[1], bounds[2], bounds[3]))
    return Ticket(fields)



def check_error_rate(ticket: Ticket) -> Tuple[int, List[str]]:
    mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
    myfile = 'data_16'

    data_16 = os.path.join(mydir, myfile)
    reached = False
    error_rate = 0
    i = 0
    correct_lines = []
    with open(data_16, 'r') as file:
        while True:
            invalid = True
            # read next line
            line = file.readline()
            # print(line)
            if not line:
                break
            name = line.split(":")[0]
            if name == "nearby tickets":
                reached = True
            if reached:
                # numbers = [int(x) for x in line.split(",") if x.isdigit()]
                numbers = re.findall(r'\d+', line)
                # print("\n")
                # print("loop {} numbers {} ".format(i, numbers))
                for number in numbers:
                    number = int(number)
                    i += 1
                    if not ticket.in_range(number):
                        print("+=",number)
                        error_rate += number
                        invalid = False
                if invalid:
                    correct_lines.append(line)


    print("total number of loops: ", i)
    return error_rate, correct_lines


ticket = create_ticket()


error_fields = check_error_rate(ticket)
print(error_fields)
lines = error_fields[1]
print(lines)

def check_done_field(fields: List[Possible]) -> bool:
    for field in fields:
        if len(field.possible_fields) > 1:
            return False
    return True

def find_to_remove(fields: List[Possible], removed: List[str]) -> str:
    for field in fields:
        if len(field.possible_fields) == 1 and field.possible_fields not in removed:
            # print("Return ",field.possible_fields)
            e = next(iter(field.possible_fields))
            return e

def remove_element(fields: List[Possible], to_remove: str) -> None:
    for field in fields:
        if field.possible_fields  != to_remove:
            # print("To remove: ",to_remove)
            if to_remove in field.possible_fields:
                # print("we remove")
                field.possible_fields.remove(to_remove)


def work_out_fields(fields: List[Possible]) -> List[Possible]:
    done = False
    removed = []
    while not done:
        to_remove = find_to_remove(fields, removed)
        removed.append(to_remove)
        remove_element(fields, to_remove)
        done = check_done_field(fields)
    return fields

def check_fields(lines: List[str]) -> int:
    fields: List[Possible] = [Possible(ticket) for i in range(20)]
    for line in lines:
        numbers = re.findall(r'\d+', line)
        for i, number in enumerate(numbers):
            temp = int(number)
            fields[i].check(temp)
    for field in fields:
        print(field.possible_fields)
    new_fields = work_out_fields(fields)
    for new_field in new_fields:
        print(new_field.possible_fields)
    return -1

check_fields(lines)

