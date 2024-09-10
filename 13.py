from typing import List, Tuple, Union

from time import time

RAW = """939
7,13,x,x,59,x,31,19"""

PUZZLE = """1011416
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,911,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,827,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"""

#question1

def time_stamp(notes: str) -> int:
    data = [x for x in notes.split("\n")]
    target = int(data[0])
    bus_ids = [ids for ids in data[1].split(",")]
    print(target, bus_ids)
    closest = float('inf')
    temp = -1
    best_id = -1
    best_count = -1
    for bus_id in bus_ids:
        if bus_id.isdigit():
            bus_id = int(bus_id)
            temp = bus_id
            count = 0
            while target > bus_id:
                bus_id += temp
                count += 1
            print("target {} bus_id {} {}".format(target, bus_id,count))
            diff = bus_id - target
            if diff < closest:
                closest = diff
                best_id = temp
                best_count = count
    print("closest {} bus {} {}".format(closest, best_id,best_count))
    return closest * best_id




# x % 7 = 0
# x % 13 = 13 - 1 -> remainder = modulo - index, modulus = modulo, number itself
# skip 2
# skip 3
# x % 59 = 59 - 4
# skip 5
# x % 31 = 31 - 6
# x % 19 = 19 - 7
#
#

def format_data(notes: str) -> List[List[Union[int, int, int]]]:
    data = [x for x in notes.split("\n")]
    if len(data) > 1:
        bus_ids = [ids for ids in data[1].split(",")]
    else:
        bus_ids = [ids for ids in data[0].split(",")]
    processed_data = []
    for i in range(len(bus_ids)):
        if bus_ids[i] != 'x':
            id = int(bus_ids[i])
            if i == 0:
                processed_data.append([id, 0, -1])
            else:
                temp = [id, (id - i) % id, -1]
                processed_data.append(temp)
    # [(remainder, modulo, inverse (=-1))]
    print("processed_data: ",processed_data)
    return processed_data

def mod_inverse(x,y):
    for i in range(y):
        if (x * i) % y == 1:
            return i

def earliest_timestamp(notes: str) -> int:
    processed_data = format_data(notes)
    N = 1
    for data in processed_data:
        N *= data[0]
    length = len(processed_data)
    answer = 0
    for i in range(length):
        remainder, modulo = processed_data[i][1], processed_data[i][0]
        n_i = N/modulo
        print("\nmod inverse: solve {} * x == 1 (mod {})".format(N/modulo,modulo))
        inverse = int(mod_inverse(n_i, modulo))
        print("Answer: {}".format(inverse))
        processed_data[i][2] = inverse
        print("Answer multiplied by remainder {} * n_i {} * inverse {} ".format(remainder, n_i, inverse ))
        answer += (remainder * n_i * inverse)
        print("answer: ",answer)
    return int(answer % N)

# print(earliest_timestamp(RAW), 1068788)
# assert earliest_timestamp(RAW) == 1068788
# assert earliest_timestamp("17,x,13,19") == 3417
# assert earliest_timestamp("67,7,59,61") == 754018
# assert earliest_timestamp("67,x,7,59,61") == 779210
# assert earliest_timestamp("67,7,x,59,61") == 1261476
# assert earliest_timestamp("1789,37,47,1889") == 1202161486

other_code = ""
print(earliest_timestamp(PUZZLE))

#COPIED CODE
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


temp = format_data(PUZZLE)
print(temp)
n, a = [], []
for i in range(len(temp)):
    n.append(temp[i][0])
    a.append(temp[i][1])
print(n)
print(a)
print(chinese_remainder(n, a))
print("diff: ",chinese_remainder(n, a)," ",earliest_timestamp(PUZZLE))

