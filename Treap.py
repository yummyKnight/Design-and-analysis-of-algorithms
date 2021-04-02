from pathlib import Path
from typing import ClassVar, Tuple, Any, Union, Optional, Iterator
from numpy.random import default_rng
import numpy as np
import copy

rng = default_rng()
info = np.iinfo(np.int64)


class Treap:
    def __init__(self, key: int = None, priority=None, left_c=None, right_c=None):
        self.key = key
        if priority is None:
            self.priority = rng.integers(info.min, info.max)
        else:
            self.priority: int = priority
        self.left_c: Treap = left_c
        self.right_c: Treap = right_c

    def copy(self, other: 'Treap'):
        self.key = other.key
        self.priority = other.priority
        self.left_c = other.left_c
        self.right_c = other.right_c

    def __repr__(self):
        return f"K-{self.key}|P-{self.priority}|" \
               f"L-{self.left_c.key if self.left_c else None}|R-{self.right_c.key if self.right_c else None}"

    def insert(self, key: int):
        left, right = Treap.split(self, key)
        new_trip = Treap(key)
        return Treap.merge(Treap.merge(left, new_trip), right)

    def search(self, key: int) -> Optional['Treap']:
        try:
            if self.key < key:
                return self.right_c.search(key)
            elif self.key > key:
                return self.left_c.search(key)
            else:
                return self
        except AttributeError:
            return None

    @staticmethod
    def merge(left: 'Treap', right: 'Treap') -> 'Treap':
        if left is None:
            return right
        if right is None:
            return left
        assert left.key < right.key
        if left.priority > right.priority:
            root = Treap(left.key, left.priority)
            root.left_c = left.left_c
            root.right_c = Treap.merge(left.right_c, right)
        elif left.priority < right.priority:
            root = Treap(right.key, right.priority)
            root.right_c = right.right_c
            root.left_c = Treap.merge(left, right.left_c)
        else:
            raise ValueError("Left and right priority are same")
        return root

    @staticmethod
    def split(trip: 'Treap', key: int) -> Tuple[Union[None, 'Treap'], Union[None, 'Treap']]:
        if trip.key < key:
            left = Treap(trip.key, trip.priority, left_c=trip.left_c)
            if trip.right_c is None:
                return left, None
            left_sub, right_sub = Treap.split(trip.right_c, key)
            left.right_c = left_sub
            right = right_sub
        else:
            right = Treap(trip.key, trip.priority, right_c=trip.right_c)
            if trip.left_c is None:
                return None, right
            left_sub, right_sub = Treap.split(trip.left_c, key)
            right.left_c = right_sub
            left = left_sub
        return left, right


def parse_input(input_path: Path) -> np.ndarray:
    with open(input_path, "r") as r:
        input_ = r.readlines()
    input_ = list(map(str.strip, input_))
    source = np.array(input_[1:], dtype=np.int64)
    return source


def parse_eval(input_path: Path) -> list:
    with open(input_path, "r") as r:
        input_ = r.readlines()
    source = list(map(str.strip, input_))
    return source


def parse_eval_2(input_path: Path) -> list:
    with open(input_path, "r") as r:
        input_ = r.readlines()
    output = []
    for line in input_:
        out1, out2 = line.split(' ')
        output.append((out1.strip(), out2.strip()))
    return output


def first_task(input_arr: np.ndarray) -> list:
    root = Treap(input_arr[0])
    out = ["-"]
    for elem in input_arr[1:]:
        if not root.search(elem):
            root = root.insert(elem)
            out.append("-")
        else:
            out.append("+")
    return out


def find_min(root: 'Treap') -> int:
    left = copy.copy(root)
    while left:
        minimal = left.key
        left = left.left_c
    return minimal


def second_task(input_arr: np.ndarray) -> list:
    root = Treap(input_arr[0])
    out1 = ["-"]
    out2 = ["-"]
    for elem in input_arr[1:]:
        desire = root.search(elem)
        if not desire:
            root = root.insert(elem)
            out1.append("-")
        else:
            out1.append("+")
        left, right = Treap.split(root, elem + 1)
        out2.append(str(find_min(right)) if right else "-")
    return list(zip(out1, out2))


def eval_1st_try(truth: list, pred: list):
    t = 0
    for i, elem in enumerate(truth):
        if elem == pred[i]:
            t += 1
    print("Correct: ", t / len(truth))


def eval_2nd_try(truth: list, pred: Iterator):
    t = 0
    for i, elems in enumerate(pred):
        if elems[0] == truth[i][0] and elems[1] == truth[i][1]:
            t += 1
    print("Correct: ", t / len(truth))


def main1():
    n_to_test = 7
    parsed = parse_input(Path(f"search_tree/{n_to_test}.in"))
    truth = parse_eval(Path(f"search_tree/{n_to_test}.contains.out"))
    pred = first_task(parsed)
    print(truth)
    print(pred)
    eval_1st_try(truth, pred)


def main2():
    n_to_test = 7
    parsed = parse_input(Path(f"search_tree/{n_to_test}.in"))
    truth = parse_eval_2(Path(f"search_tree/{n_to_test}.min-after.out"))
    pred = second_task(parsed)
    print(list(pred))
    print(truth)
    eval_2nd_try(truth, pred)


if __name__ == '__main__':
    main2()
