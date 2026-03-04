# Authored by : 21011645
# https://www.acmicpc.net/problem/10093

import sys

input = sys.stdin.readline


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def main() -> None:
    A, B = map(int, sys_input().split())

    answer: int = B - A - 1
    print(answer)
    for i in range(A + 1, B):
        print(i, end=" ")


if __name__ == "__main__":
    main()
