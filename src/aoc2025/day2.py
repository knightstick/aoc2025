from aoc2025.utils import load_day


def main():
    input = load_day(2)
    print(part_one(input))
    print(part_two(input))


def part_one(input: str):
    ranges = [range.split("-") for range in input.strip().split(",")]
    invalid_ids = []

    for [start, finish] in ranges:
        start = int(start)
        finish = int(finish)

        for i in range(start, finish + 1):
            i = str(i)
            half = len(i) // 2
            first = i[:half]
            second = i[half:]

            if first == second:
                invalid_ids.append(int(i))

    return sum(invalid_ids)


def part_two(input: str):
    ranges = [range.split("-") for range in input.strip().split(",")]
    invalid_ids = []

    for [start, finish] in ranges:
        finish_len = len(finish)
        half = finish_len // 2

        start = int(start)
        finish = int(finish)

        inner_invalid_ids = []

        for i in range(1, 10**half):
            i = str(i)
            digits = i + i

            while len(digits) <= finish_len:
                candidate = int(digits)

                if candidate >= start and candidate <= finish:
                    inner_invalid_ids.append(candidate)

                digits = digits + i

        invalid_ids = invalid_ids + list(set(inner_invalid_ids))

    return sum(invalid_ids)


if __name__ == "__main__":
    main()
