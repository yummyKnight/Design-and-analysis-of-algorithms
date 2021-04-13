import numpy as np
import typing as ty
import matplotlib.pyplot as plt


class BinarySearchByVal:

    def __init__(self, array: np.ndarray, amount: int):
        self.array = array
        self.amount = amount

    def perform(self) -> int:
        left = -1
        right: int = (self.array[-1] - self.array[0]) // self.amount
        while right - left > 1:
            mid: int = (right + left) // 2
            if self._check(mid):
                right = mid
            else:
                left = mid
            # print("Debug: ", right, left)
        return right

    def _check(self, size: int) -> bool:
        start = 0
        closed_points = 0
        arr_len = len(self.array)
        for _ in range(self.amount):
            closed_points += 1
            for i in range(start + 1, arr_len):
                if self.array[i] - self.array[start] > size:
                    start = i
                    break
                closed_points += 1
            # есть случаи когда отрезки настолько длинные что покрывают все точки за меньшее K,
            # но без этого условия check вернет false из за строчек 27-28, поэтому нужно либо
            # проверять что все точки покрыты после каждого прохода
            # 1го цикла либо ставить условие closed_points >= arr_len
            if closed_points == arr_len:
                return True
        return False

    def __repr__(self):
        return f"k - {self.amount}, array - {self.array}"

    def __str__(self):
        return f"k - {self.amount}, array - {self.array}"


def parse_input(path_to_input: str) -> ty.Tuple[np.ndarray, int]:
    with open(path_to_input, "r") as r:
        input_ = r.readlines()
    input_ = list(map(str.strip, input_))
    k = int(input_[1])
    source = np.array(input_[2:], dtype=np.int64)
    return source, k


if __name__ == '__main__':
    source_arr, amount = parse_input("BSVTESTS/5.in")
    print(BinarySearchByVal(source_arr, amount).perform())
