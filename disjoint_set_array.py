from pathlib import Path
from typing import Tuple, List
import numpy as np


def parse_input(input_path: Path) -> Tuple[int, int, np.ndarray]:
    with open(input_path, "r") as r:
        input_ = r.readlines()
    source = list(map(str.split, input_))
    n = int(source[0][0])
    amount = int(source[0][1])
    output = np.array([[int(a), int(b)] for a, b in source[1:]])
    return n, amount, output


def parse_output(out_path: Path) -> np.ndarray:
    with open(out_path, "r") as r:
        input_ = r.readlines()
    source = np.array(list(map(lambda x: True if x == "YES" else False, map(str.strip, input_))))
    return source


class DSA:
    def __init__(self, size: int):
        self.parents = np.arange(size, dtype=int)

    def find(self, a: int):
        if a == self.parents[a]:
            return a
        else:
            self.parents[a] = self.find(self.parents[a])
            return self.parents[a]

    def unite(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)
        # self.parents[root_b] = root_a
        rand = np.random.randint(2, size=1)
        if rand[0] == 0:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a

    def test(self, a: int, b: int):
        if self.find(a) == self.find(b):
            return True
        else:
            return False


def main():
    name = "4"
    size, amount, pairs_of_elems = parse_input(Path(f"UFF_TESTS/{name}.in"))
    check = parse_output(Path(f"UFF_TESTS/{name}.out"))
    dsa = DSA(size)
    alg_res = np.zeros(shape=(amount,), dtype=bool)
    for i in range(amount):
        a, b = pairs_of_elems[i]
        part_res = dsa.test(a, b)
        if not part_res:
            dsa.unite(a, b)
        else:
            alg_res[i] = True
    result = np.sum(np.bitwise_xor(alg_res, check))
    print(1 - result / amount)


if __name__ == '__main__':
    main()
