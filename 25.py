

def get_loop_size(key: int) -> int:
    num = 1
    done = False
    i = 0
    while not done:
        num *= 7
        num = (num % 20201227)
        if num == key:
            done = True
        i += 1
    return i

def get_answer(subject_num: int, loop_size) -> int:
    start = 1
    for _ in range(loop_size):
        start *= subject_num
        start = (start % 20201227)
    return start


def encryption(card_key: int, door_key: int) -> int:
    card_loop_size = get_loop_size(card_key)
    door_loop_size = get_loop_size(door_key)
    assert get_answer(card_key, door_loop_size) == get_answer(door_key, card_loop_size)
    return get_answer(card_key, door_loop_size)
print(get_loop_size(5764801))
# encryption(5764801, 17807724)#card public key
#door public key
#PUZZLE:
# 13233401
# 6552760
print(encryption(13233401, 6552760))