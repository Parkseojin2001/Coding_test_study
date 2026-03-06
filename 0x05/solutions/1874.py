# Authored by : 21011645
# https://www.acmicpc.net/problem/1874
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(sequence: list[int]) -> str:
    stack = []
    ops = []
    curr = 1

    for c in sequence:
        while curr <= c:
            stack.append(curr)
            ops.append("+")
            curr += 1

        if not (stack and stack[-1] == c):
            return "NO"

        stack.pop()
        ops.append("-")

    return "\n".join(ops)


def main() -> None:
    n = int(sys_input())
    sequence = [int(sys_input()) for _ in range(n)]

    answer: str = solve(sequence)
    print(answer)


if __name__ == "__main__":
    main()
