import numpy as np
import typing as ty

def bs_by_value(array : np.ndarray, amount : int):
    pass



def parse_input(path_to_input: str) -> ty.Tuple[np.ndarray, int]:
    with open(path_to_input, "r") as r:
        input_ = r.readlines()
    input_ = list(map(str.strip, input_))
    k = int(input_[1])
    print(k)
    source = np.array(input_[2:], dtype=np.int64)
    print(source)
    return source, k


if __name__ == '__main__':
    # start_sum()
    source, to_find = parse_input("BSVTESTS/1.in")
    # for val in to_find:
    #     print(binary_search(source, val))
