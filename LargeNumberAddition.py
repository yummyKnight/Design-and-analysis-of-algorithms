class BigNumber:
    def __init__(self, representation: str):
        self.repr = representation

    def __add__(self, other):
        bigger = self.repr
        smaller = other.repr
        if len(bigger) < len(smaller):
            bigger, smaller = other.repr, self.repr

        bigger = bigger[::-1]
        smaller = smaller[::-1]
        res = []
        carry = 0
        for i in range(len(smaller)):
            part_sum = int(bigger[i]) + int(smaller[i]) + carry
            carry = part_sum // 10
            res.append(part_sum % 10)
        pos = len(smaller)
        while carry == 1 and pos < len(bigger):
            part_sum = int(bigger[pos]) + carry
            carry = part_sum // 10
            res.append(part_sum % 10)
            pos += 1
        if carry == 1:
            res.append("1")
        else:
            res.append(bigger[pos:])
        return BigNumber("".join(map(str, res))[::-1])

    def __str__(self) -> str:
        return self.repr

    def __repr__(self) -> str:
        return str(self)


def start_sum() -> list:

    with open("input.txt", "r") as r:
        input_ = r.readlines()
    answers = []
    n = int(input_[0])
    for i in range(1, n + 1):
        first, second = input_[i].split()
        answers.append(str(BigNumber(first) + BigNumber(second)))
    return answers


def test(prog_answers: list):
    with open("test.out", "r") as r:
        answers = r.readlines()
    for i, answer in enumerate(answers):
        if answer.strip() == prog_answers[i]:
            print("TRUE")
        else:
            print("FALSE")
            print(answer)
            print(prog_answers[i])


if __name__ == '__main__':
    test(start_sum())
