import itertools
from aoc2025.utils import load_day_lines

test_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


def main():
    input = test_input.strip().splitlines()
    input = load_day_lines(3)

    print(part_one(input))
    print(part_two(input))


def part_one(lines: list[str]):
    return sum(joltage(bank) for bank in lines)


def part_two(lines: list[str]):
    return sum(joltage(bank, 12) for bank in lines)


def joltage(bank: str, length: int = 2, acc: list[str] = []):
    bank_len = len(bank)
    parts = []

    start = 0
    to_find = length
    end = bank_len - to_find + 1

    while start < end and to_find > 0:
        x = 0
        for i in range(start, end):
            digit = int(bank[i])
            if digit > x:
                x = digit
                start = i + 1

        parts.append(str(x))
        to_find -= 1
        end = bank_len - to_find + 1

    return int("".join(parts))


# Works in theory, but, didn't finish
def _joltage(bank: str, length: int = 2):
    max = 0

    for jolt in (int("".join(x)) for x in itertools.combinations(bank, length)):
        if jolt > max:
            max = jolt

    return max


# BR00T FORCE, also works in theory
def __joltage(bank: str):
    max = 0
    bank_len = len(bank)

    for i in range(bank_len):
        for j in range(i + 1, bank_len):
            jolt = int("".join([bank[i], bank[j]]))

            if jolt > max:
                max = jolt

    return max


if __name__ == "__main__":
    main()
