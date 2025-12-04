from aoc2025.utils import load_day_lines

type Coord = tuple[int, int]
type Grid = dict[Coord, str]


def main():
    input = load_day_lines(4)

    print(part_one(input))
    print(part_two(input))


def part_one(lines: list[str]):
    grid = parse_grid(lines)

    return len(available_rolls(grid))


def part_two(lines: list[str]):
    grid = parse_grid(lines)
    available = available_rolls(grid)
    result = 0

    while len(available) > 0:
        for coord in available_rolls(grid):
            grid[coord] = "."
            result += 1

        available = available_rolls(grid)

    return result


def available_rolls(grid: Grid) -> list[Coord]:
    return [
        coord
        for coord, val in grid.items()
        if val == "@" and neighbours(grid, coord) < 4
    ]


def parse_grid(lines: list[str]) -> Grid:
    grid: dict[tuple[int, int], str] = {}

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            grid[(j, i)] = char

    return grid


def neighbours(grid: Grid, coord: Coord) -> int:
    (x, y) = coord

    adjacent = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]

    return sum(
        grid[(x + dx, y + dy)] == "@" for dx, dy in adjacent if (x + dx, y + dy) in grid
    )


if __name__ == "__main__":
    main()
