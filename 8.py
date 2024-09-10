import os

from typing import Dict, Tuple, List, Union


mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_8'
data_8 = os.path.join(mydir, myfile)
data = []

def get_action_val(command_line: str) -> List[Union[str, int, bool]]:
    command, action = command_line.split()

    if action[0] == "+":
        action = int(action[1:])
    else:
        action = -1*int(action[1:])
    return [command, action, False]

def create_data():
    i = 0
    line_to_command_dict: Dict[int, Tuple[str,int,bool]] = {}
    with open(data_8,'r') as file:
        while (True):
            # read next line
            line = file.readline()
            if not line:
                break
            line_to_command_dict[i] = get_action_val(line)
            i += 1
    return line_to_command_dict
line_to_command_dict = create_data()
def change_values(accumulator : int, iterator: int, command: str, action: int) -> Tuple[int, int]:
    # print("Accumulator {} iterator {} command {} action {} ".format(accumulator, iterator, command, action))
    if command == "nop":
        return (accumulator, iterator+1)
    elif command == "jmp":
        return (accumulator, iterator+action)
    elif command == "acc":
        return (accumulator+action, iterator+1)
    else:
        print("\n\nERROR ", command)

accumulator: int = 0
iterator: int = 0

def do_stuff(dict) -> (int,bool):
    size_dict = len(dict.keys())
    accumulator: int = 0
    iterator: int = 0
    while True:
        try:
            command, action, had_before = dict.get(iterator)
        except:
            print("\n\nWE BREAK on iterator {} ".format(iterator))
            if iterator >= size_dict:
                print("Correct break")
                return (accumulator, True)
            else:
                print("WE broke wrong, made a mistake")
                return (accumulator, False)
        del dict[iterator]
        temp = change_values(accumulator, iterator, command, action)
        accumulator, iterator = temp[0], temp[1]




def get_error_iterator(dict) -> List[Tuple[int,str,bool]]:
    accumulator: int = 0
    iterator: int = 0
    command, action = -1, ""
    prev_iterator = -1
    iter_action: List[Tuple[int,str,bool]] =[]
    while True:
        # print(dict)
        command, action, had_before = dict.get(iterator)
        iter_action.append((iterator,command,had_before))
        if had_before:
            return iter_action
        dict[iterator][2] = True
        temp = change_values(accumulator, iterator, command, action)
        accumulator, iterator = temp[0], temp[1]


def change(command: str) -> str:
    changed = ""
    if command == "jmp":
        changed = "nop"
    elif command == "nop":
        changed = "jmp"
    return changed

# print(do_stuff(line_to_command_dict))
#
copy_dict = dict(line_to_command_dict)
error_list = get_error_iterator(copy_dict)
print(error_list[::-1])

#change elements untill we finish the program
#so we'll have to move until

#
first = False
second = False
to_change = None
print("Check before: " ,line_to_command_dict[526])
for tuple in reversed(error_list):
    line_to_command_dict = create_data()
    position, command = tuple[0], tuple[1]
    if command == "jmp" or command == "nop":
        to_change = tuple
        print("We check this tuple: ",to_change)
        changed_command = change(to_change[1])
        line_to_command_dict[to_change[0]][0] = changed_command
        temp = do_stuff(line_to_command_dict)
        if temp[1]:
            break

print(temp)