from typing import List


# TODO refactoring
class Node:
    def __init__(self, value: int):
        self.value = value
        self.parent = None


class UnionFind:
    def __init__(self, arr: List[int]):
        self.arr: List['Node'] = []
        for elem in arr:
            self.arr.append(Node(elem))

    # @staticmethod
    def find(self, a: int):
        for x in self.arr:
            if x.value == a:
                current = x
                break
        while current.parent:
            current = current.parent
        return current

    def unite(self, a: int, b: int):
        self.find(a).parent = self.find(b)

    def test(self, a: int, b: int):
        val_a = None
        val_b = None
        for x in self.arr:
            if x.value == a:
                val_a = x
            if x.value == b:
                val_b = x
            if val_a and val_b:
                break
        return self.find(a) == self.find(b)


def start_union():
    # n = int(input())
    n, m = map(int, input().split())
    a = [i for i in range(n)]
    union = UnionFind(a)
    # k = int(input())
    for i in range(m):
        x, y = map(int, input().split())
        flag = union.test(x, y)
        if not flag:
            union.unite(x, y)
        print("YES" if flag else "NO")


if __name__ == '__main__':
    start_union()
