from aoc2025.utils import load_day_lines

test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def main():
    input = load_day_lines(1)

    print(part_one(input))
    print(part_two(input))


def part_one(input: list[str]):
    positions = []

    position = 50
    positions.append(position)

    for instruction in input:
        position = new_position(position, instruction)
        positions.append(position)

    return sum(pos == 0 for pos in positions)


def part_two(input: list[str]):
    zeroes = 0
    position = 50

    for instruction in input:
        [dir, *digits] = list(instruction)
        degrees = int("".join(digits))

        match dir:
            case "L":
                for _ in range(degrees):
                    position = (position - 1) % 100

                    if position == 0:
                        zeroes += 1
            case "R":
                for _ in range(degrees):
                    position = (position + 1) % 100

                    if position == 0:
                        zeroes += 1

    return zeroes


def new_position(pos: int, inst: str) -> int:
    [dir, *digits] = list(inst)
    degrees = int("".join(digits))

    match dir:
        case "L":
            return (pos - degrees) % 100
        case "R":
            return (pos + degrees) % 100
        case _:
            raise ValueError


if __name__ == "__main__":
    main()
