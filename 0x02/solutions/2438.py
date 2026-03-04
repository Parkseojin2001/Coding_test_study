# Authored by : 21011645
# https://www.acmicpc.net/problem/2438
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def stars(n: int) -> str:
    return "*" * n


def main() -> None:
    N = int(sys_input())
    for i in range(1, N + 1):
        print(stars(i))


if __name__ == "__main__":
    main()
