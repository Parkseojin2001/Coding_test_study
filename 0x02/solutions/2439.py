# Authored by : 21011645
# https://www.acmicpc.net/problem/2439
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def stars(n: int, m: int) -> str:
    return " " * (m - n) + "*" * n


def main() -> None:
    N = int(sys_input())
    for i in range(1, N + 1):
        print(stars(i, N))


if __name__ == "__main__":
    main()
