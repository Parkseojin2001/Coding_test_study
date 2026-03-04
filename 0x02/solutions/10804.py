# Authored by : 21011645
# https://www.acmicpc.net/problem/10804

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(intervals: list[tuple[int, int]]) -> list[int]:
    cards = list(range(1, 21))
    for a, b in intervals:
        cards[a - 1 : b] = cards[a - 1 : b][::-1]

    return cards


def main() -> None:
    intervals = [tuple(map(int, sys_input().split())) for _ in range(10)]

    answer: list[int] = solve(intervals)
    print(*answer)


if __name__ == "__main__":
    main()
