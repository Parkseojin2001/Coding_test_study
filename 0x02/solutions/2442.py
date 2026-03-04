# Authored by : 21011645
# https://www.acmicpc.net/problem/2442
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def stars(n: int, m: int) -> str:
    return " " * (m - n) + "*" * (2 * n - 1)


def main() -> None:
    N = int(sys_input())
    for i in range(1, N + 1):
        print(stars(i, N))


if __name__ == "__main__":
    main()
