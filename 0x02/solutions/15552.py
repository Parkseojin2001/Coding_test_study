# Authored by : 21011645
# https://www.acmicpc.net/problem/15552
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(pairs: list[int]) -> list[int]:
    return [a + b for a, b in pairs]


def main() -> None:
    T = int(sys_input())
    pairs = [tuple(map(int, sys_input().split())) for _ in range(T)]

    answers: list[int] = solve(pairs)

    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()
