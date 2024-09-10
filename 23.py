from typing import List
from time import time


#shift if the indices are 0, 1 or 2
#first, create a new ordering then do the shifting

class Game:
    def __init__(self, rounds: int = 10):
        self.destination_cup = -1
        self.rounds = rounds
        self.cups = []

    def create_data(self, input: str) -> None :
        self.cups: List[int] = []
        for num in input:
            self.cups.append(int(num))
        self.current_cup = self.cups[0]
        #create a new one, otherwise the length will vary
        temp = self.cups[::]
        self.LENGTH = len(temp)+1


    def create_data2(self, input: str) -> None:
        self.cups = [int(x) for x in input]
        max_n = max(self.cups)
        for i in range(max_n + 1, 1000000 + 1):
            self.cups.append(i)
        self.current_cup = self.cups[0]
        # create a new one, otherwise the length will vary
        temp = self.cups[::]
        self.LENGTH = len(temp) + 1


    def get_destination_cup(self) -> int:
        target = (self.current_cup -1) % self.LENGTH
        while True:
            if target == 0:
                target = self.LENGTH-1
            if target not in self.removed:
                # print("destination cup: ", target)
                return target
            target = (target -1) % self.LENGTH

    def get_index(self, l: List[int], cup_value: int) -> int:
        for i, num in enumerate(l):
            # print("check index ",i)
            if num == cup_value:
                return i


    def change_order(self):
        # print("New current cup index: ",self.get_index(self.cups, self.current_cup))
        # print("Original current cup index ",self.get_index(self.cups, self.current_cup))
        new_first, new_last = [], []
        new_cup_index = self.get_index(self.cups, self.current_cup)
        if self.destination_index < self.current_cup_index:
            pass
        if new_cup_index != self.current_cup_index:
            print("\n\n\n Diff ",new_cup_index-self.current_cup_index)
            # print("The current list ",self.cups)
            # print("Split index: ",(new_cup_index-self.current_cup_index))
            debug = True
            if not debug:
                new_first[:] = self.cups[(new_cup_index-self.current_cup_index):]
                new_last[:] = self.cups[:(new_cup_index-self.current_cup_index)]
                print("\n-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0\nnew first: ",new_first)
                print("new last  ", new_last)

                self.cups = self.cups[(new_cup_index-self.current_cup_index):] + self.cups[:(new_cup_index-self.current_cup_index)]
                self.cups = new_first + new_last

                print("The new cups: ", self.cups)
                print("-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0\n")
            else:
                # print("enter the fancy debug stage")
                for i in range((new_cup_index-self.current_cup_index)):
                    popped = self.cups.pop(0)
                    # print(f"Move {popped} to the end")
                    self.cups.append(popped)

            # print("\n-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0")
            # print("The new cups: ", self.cups)
            # print("-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0\n")
    def step(self, current_cup_index: int) -> None:
        """
        Observe that the current index is invariant
        """
        # self.current_cup_index = self.get_index(self.cups, self.current_cup)
        self.current_cup_index = current_cup_index
        self.removed = [self.cups[i % 9] for i in range(self.current_cup_index+1,self.current_cup_index+3+1)]
        # print("Current cup {} current list {}".format(self.current_cup, self.cups))
        # print("we self.removed ",self.removed)
        for x in self.removed:
            self.cups.remove(x)
        # print("The cups after deleting {} ".format(self.cups))
        #insert the cups to the right of the target
        self.destination_cup = self.get_destination_cup()
        self.destination_index = self.get_index(self.cups, self.destination_cup)
        # print("Destination cup: ",self.destination_cup)
        # print("Destination index: ",self.destination_index)
        for i, num in enumerate(self.removed):
            insert_idx = self.destination_index + i + 1
            self.cups.insert(insert_idx, num)
        # print("The 'inserted' list ",self.cups)
        self.change_order()
        #Set the new current cup
        self.current_cup = self.cups[(self.current_cup_index+1) % 9]

    def find_answer_2(self) -> int:
        for i, num in enumerate(self.cups):
            if num == 1:
                return self.cups[(i + 1) % 9]*self.cups[(i + 2) % 9]

    def play(self):
        begin = time()
        for _ in range(self.rounds):
            # print(f"Round {_+1} ")
            if ((_+1) % 100) == 0:
                print(f"Round {_+1}, time {time()-begin}")
                begin = time()
            self.step((_ % self.LENGTH))


from dataclasses import dataclass

class Node:
    def __init__(self, value: int, next) -> None:
        self.value: int = value
        self.next: Node = next

class CupGame2:
    """
    The smart way of doing it, using a linked list.
    """
    def __init__(self, input: str):
        cups = [int(x) for x in input]
        cups.extend(range(10, 1_000_001))
        #Create a Linked List
        #We'll do so by using a dictionary (--> constant lookup time :))
        self.current = prev = cups[0]
        #so now the first element links to the second element
        self.linked_cups = {self.current: Node(self.current, None)}
        #add forward links
        for cup in cups[1:]:
            #create a new element in the list, not yet connected
            self.linked_cups[cup] = Node(cup, None)
            #connect the previous node with the new node
            self.linked_cups[prev].next = self.linked_cups[cup]
            prev = cup
        #link the last cup to the first cup
        self.linked_cups[cup].next = self.linked_cups[self.current]

        # self.get_10(3)

        assert len(self.linked_cups.keys()) == 10**6


    def move(self):
        #we start of with the correct current value.
        current = self.linked_cups[self.current]
        # print("\n\n")
        # self.get_10(current.value)
        # self.get_10(3)
        #get the next 3 nodes and their values
        node_1 = current.next
        node_2 = node_1.next
        node_3 = node_2.next
        addit = node_3.next

        v1 = node_1.value
        v2 = node_2.value
        v3 = node_3.value
        #create 'new' links between the current and the addit.
        #in this way, we are skipping the 3 nodes, sort of removing them
        #but not exactly. In the dict (the linked list) their corresponding
        #values still map to the nodes. So they are not removed from the LL
        #but rather skipped.
        current.next = addit
        # print("move")
        # self.get_10(3)
        #disconnect them
        # node_1.next = node_1.value = node_2.next = node_2.value = node_3.next = node_3.value = None

        #now we need to know where to insert the 3 'deleted' nodes
        #that is, we need to find the destination
        destination = current.value -1 if current.value > 1 else 10**6
        while destination in [v1, v2, v3]:
            destination = destination - 1 if destination > 1 else 10 ** 6
        # print(f"Destination {destination}")
        #now insert the cups after the destination
        new_1 = Node(v1, None)
        new_2 = Node(v2, None)
        new_3 = Node(v3, None)

        dest_cup = self.linked_cups[destination]
        addit = dest_cup.next
        dest_cup.next = new_1
        new_1.next = new_2
        new_2.next = new_3
        new_3.next = addit

        #now make sure that the values link to the correct nodes
        #not sure if needed. EDIT: probably needed
        self.linked_cups[v1] = new_1
        self.linked_cups[v2] = new_2
        self.linked_cups[v3] = new_3
        # print(self.linked_cups[v1].value)
        #set the new current
        # print(f"look for {current.value} ")
        self.current = self.linked_cups[current.value].next.value


    def get_10(self, init: int):
        current = self.linked_cups[init]
        s = []
        for _ in range(10):
            s.append(current.value)
            current = current.next
        print(s)


RAW = """389125467"""
PUZZLE = """789465123"""

game = CupGame2(PUZZLE)
for _ in range(10_000_000):
    if _ % 1000 == 0:
        print(_)
    game.move()

game.get_10(1)
print(f"result {game.linked_cups[1].next.value*game.linked_cups[1].next.next.value} ")
# for _ in range(10):
#     game.move()
#     # game.get_10(3)
#




