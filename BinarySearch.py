import numpy as np
import typing as ty


def binary_search(array: np.ndarray, val: int):
    left = -1
    right = len(array)
    while right > left + 1:
        middle = (left + right) // 2
        if array[middle] == val:
            return middle
        if array[middle] > val:
            right = middle
        else:
            left = middle
    return -1


# Press the green button in the gutter to run the script.
def start_binary():
    a = np.array(map(int, input().split()))
    x = int(input())
    print(binary_search(a, x))


def parse_input(path_to_input: str) -> ty.Tuple[np.ndarray, np.ndarray]:
    with open(path_to_input, "r") as r:
        input_ = r.readlines()
    input_ = list(map(str.strip, input_))
    source = np.array(input_[1].split(), dtype=np.int64)
    print(source)
    to_find = np.array(input_[3:], dtype=np.int64)
    print(to_find)
    return source, to_find


if __name__ == '__main__':
    # start_sum()
    source, to_find = parse_input("BSTESTS/4.in")
    for val in to_find:
        print(binary_search(source, val))
