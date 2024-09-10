from typing import Tuple, List

class Queue:
    """
    A class to maintain a queue.
    This is used for the vertices that have 'too much ' probability stored in them.
    """
    def __init__(self):
        self.queue = []

    def dequeue(self):
        """
        Remove the first element from the queue
        :return: the removed element
        """
        if len(self.queue)>0:
            return self.queue.pop(0)

    def enqueue(self,element):
        """
        Add an element (vertex label, integer) to the end of the queue
        :param element: (in this context) integer, a vertex label
        :return: void
        """
        # print("We want to add",element,". The elements already in the queue are: ",self.already_in_queue," The queue: ",self.queue)
            # print("We add: ",element)
        self.queue.append(element)

    def getLength(self):
        return len(self.queue)

    def get_queue(self):
        copy = self.queue[::]
        return copy

    def print(self):
        print("-Updated Queue-\n",self.queue,"\n---")


def init_queues() -> Tuple[Queue, Queue]:
    p1, p2 = Queue(), Queue()
    reachedp2 = False
    with open('C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data\\data_22') as f:
        while True:
            line = f.readline()
            line = line.strip()
            if not line:
                break
            if line == "Player 2:":
                reachedp2 = True
            print(line, reachedp2)

            if line.isdigit():
                if not reachedp2:
                    p1.enqueue(int(line))
                else:
                    p2.enqueue((int(line)))
    return p1, p2

def get_score(player: Queue) -> int:
    score = 0
    total_cards = len(player.queue)
    for i, card in enumerate(player.queue):
        score += (total_cards-i)*card
    return score


def check_queue(p1: Queue, p2: Queue, checked1: List[List[int]], checked2: List[List[int]]) -> bool:
    # print("\no-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o\nChecking the queues")
    # print("p1 queue {} played 1 {} ".format(p1.queue, checked1))
    # print("p2 queue {} played 2 {} ".format(p2.queue, checked2))
    return p1.queue in checked1 and p2.queue in checked2

def play(player1: Queue, player2: Queue) -> str:
    winner = None
    total = 0
    played_hands1, played_hands2 = [], []
    prev1, prev2 = None, None
    while player1.getLength() > 0 and player2.getLength() > 0:
        if prev1 == player1.queue and prev2 == player2.queue:
            return "p1"
        if total > 5000:
            return ""
        prev1, prev2 = player1.get_queue(), player2.get_queue()

        # print("\nPlayer 1: ", player1.queue)
        # print("Player 2: ", player2.queue)
        card1, card2 = player1.dequeue(), player2.dequeue()
        if card1 <= player1.getLength() and card2 <= player2.getLength():
            new_p1, new_p2 = Queue(), Queue()
            for i, card in enumerate(player1.queue):
                if i < card1:
                    new_p1.enqueue(card)
            for i, card in enumerate(player2.queue):
                if i < card2:
                    new_p2.enqueue(card)
            # print("\n\n\n\n\n\n\n\n\n\n------------------------\nenter a subgame with")
            # print("1 card1 {} , new stack p1 {} ".format(card1, player1.queue))
            # print("2 card2 {} , new stack p2 {} ".format(card2, player2.queue))
            winner = play(new_p1, new_p2)
        if winner is not None:
            if winner == "p1":
                player1.enqueue(card1)
                player1.enqueue(card2)
                winner = None
            elif winner == "p2":
                player2.enqueue(card2)
                player2.enqueue(card1)
                winner = None
            else:
                raise ValueError("wrong return in winner namely {} ".format(winner))
        else:
            if card1 > card2: #p1 wins
                player1.enqueue(card1)
                player1.enqueue(card2)
            elif card2 > card1:
                player2.enqueue(card2)
                player2.enqueue(card1)
            else:
                raise ValueError("Cards have the same value")
        total += 1
        if check_queue(player1, player2, played_hands1, played_hands2):
            # print("\n\n\n\n\n ----------------------------------------------------------------\n"
            #       "We have the same stuff")
            return "p1"
        else:
            played_hands1.append(player1.get_queue())
            played_hands2.append(player2.get_queue())

    if player1.getLength() > 0:
        print("player 1  won")
        print("Score: ",get_score(player1))
        return "p1"
    else:
        print("player 2  won")
        print("Score: ",get_score(player2))
        return "p2"


p1, p2 = init_queues()
print(p1.queue, p2.queue)
winner = play(p1, p2)


RAW = """Player 1:
9
2
6
3
1
Player 2:
5
8
4
7
10"""
