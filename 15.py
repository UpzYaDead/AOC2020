RAW1 = """0,3,6"""
RAW2 = """1,3,2"""
RAW3 = """2,1,3"""
RAW4 = """1,2,3"""
RAW5 = """2,3,1"""
RAW6 = """3,2,1"""
RAW7 = """3,1,2"""

PUZZLE = """16,1,0,18,12,14,19"""

from typing import Dict, List

def init_game(input: str) ->  Dict[int, List[int]]:
    spoken_before: Dict[int, List[int]] = {}
    numbers = input.split(",")
    for i, number in enumerate(numbers):
        spoken_before[int(number)] = [i+1]
    return spoken_before

print(init_game(RAW1))
def update_spoken(spoken_before: Dict[int, List[int]], new_num: int, turn: int) -> Dict[int, List[int]]:
    if new_num not in spoken_before.keys():
        spoken_before[new_num] = [turn]
    else:
        spoken_before[new_num].append(turn)
    return spoken_before

def memory_game(spoken_before: Dict[int, List[int]], turns: int = 2020) -> int:
    turn = len(spoken_before.keys())+1
    new_num = 0 #by default, always true
    while turn < turns:
        # print("\n\nturn {} Spoken before {} ".format(turn, spoken_before))
        if (turns % 5000000) == 0:
            print("current turn is ",turn)
        spoken_before = update_spoken(spoken_before, new_num, turn)
        if len(spoken_before[new_num]) > 1:
            new_num = spoken_before[new_num][-1] - spoken_before[new_num][-2]
        else:
            new_num = 0
        turn += 1
    return new_num



def run(input: str):
    spoken_before = init_game(input)
    return memory_game(spoken_before, turns = 30000000)

print(run(PUZZLE))

