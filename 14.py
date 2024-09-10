import os

import re

from typing import List, Dict

import itertools

def get_bin(x, n=36):
    return format(x, 'b').zfill(n)

def to_base_10(b_2: str) -> int:
    b_10 = 0
    for i, digit in enumerate(reversed(b_2)):
        b_10 += int(digit) * (2**i)
    return b_10



class Memory:
    def __init__(self):
        self.memory = {}

    def apply_mask(self) -> None:
        """
        Apply the mask to the value, decode
        'masked value' and write it to the address.
        """
        mask, value = list(self.current_mask), list(self.value)
        # print(len(mask), len(value))
        for i, m in enumerate(mask):
            if m != "X":
                value[i] = m
        value = "".join(value)
        #decode the 'masked' value and write to the adress
        print(to_base_10(value))
        self.memory[self.address] = to_base_10(value)

    def read_input(self):
        mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
        myfile = 'data_14'
        data_14 = os.path.join(mydir, myfile)
        f = open(data_14, "r")
        t = 1
        while True:
            line = f.readline().strip()
            if not line:
                break
            if re.match('^mask', line):
                self.current_mask = line.split("mask = ")[1]
                print(self.current_mask)
            else:
                self.address = int(re.findall('\[(.*)\]',line)[0])
                self.value = int(line.split(" = ")[1])
                print("New value, ",t)
                t += 1
                #encode the value
                self.value = get_bin(self.value)
                print(self.address, self.value)
                self.apply_mask()

class Memory2:
    def __init__(self):
        self.memory = {}
        self.got_permutations: Dict[int: List[int]] = {}

    def apply_mask(self) -> None:
        """
        Apply the mask to the value, decode
        'masked value' and write it to the address.
        """
        mask, address = list(self.current_mask), list(get_bin(self.address))
        for i, m in enumerate(mask):
            if m != "0":
                address[i] = m

        # value = "".join(value)
        addresses = self.address_permutations(address)
        for add in addresses:
            # print("Write to: ", add)
            self.memory[add] = self.value

    def address_permutations(self, address: List[str]) -> List[int]:
        address_str = "".join(address)
        num_X = len(re.findall(r'X',address_str))
        # print(num_X)
        all_combinations = []
        temp = []
        if not self.got_permutations.get(num_X):
            temp1 = set()
            for i in range(1,num_X+1):
                x_s = [1]*(i-1)
                while len(x_s) < num_X:
                    x_s.append(0)
                #now we have a list with i number of zeros
                #get all the possible combinations
                combinations = {comb for comb in itertools.permutations(x_s, len(x_s))}
                combinations.add(tuple([0]*num_X))
                combinations.add(tuple([1]*num_X))
                temp1 = temp1 | combinations
                # print(f"iter: {i} temp1 {temp1}")
                # print("comb: ",combinations)

            self.got_permutations[num_X] = temp1
            combinations = temp1
        else:
            combinations = self.got_permutations[num_X]
        # print(f"All the comb {num_X}  are {combinations}")
        for comb in combinations:
            j = 0
            copy_address = list(address_str[::])
            for i, num in enumerate(address_str):
                if num == "X":
                    copy_address[i] = str(comb[j])
                    j += 1
            temp.append(copy_address)
            # print("TEMP: ", temp)
            copy_address = "".join(copy_address)
            # print(copy_address)
            all_combinations.append(to_base_10(copy_address))
        return all_combinations

    def read_input(self):
        mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
        myfile = 'data_14'
        data_14 = os.path.join(mydir, myfile)
        f = open(data_14, "r")
        while True:
            line = f.readline().strip()
            if not line:
                break
            if re.match('^mask', line):
                self.current_mask = line.split("mask = ")[1]
                print(self.current_mask)
            else:
                self.address = int(re.findall('\[(.*)\]',line)[0])
                self.value = int(line.split(" = ")[1])
                #encode the value
                self.apply_mask()


mem = Memory2()
mem.read_input()

total = 0
for val in mem.memory.values():
    total += val
print(mem.memory)
print(total)
