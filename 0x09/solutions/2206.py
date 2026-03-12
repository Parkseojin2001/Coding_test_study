# Authored by : 21011645
# https://www.acmicpc.net/problem/2206
import sys
from collections import deque

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def bfs(n: int, m: int, maps: list[str]) -> list[list[tuple[int, int]]]:
    deq = deque([(0, 0)])
    dist = [[[-1, 1]for _ in range(m)] for _ in range(n)]
    dist[0][0][0] = 0
    while deq:
        x, y = deq.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == "0":
                    dist[nx][ny][0] = dist[x][y][0] + 1
                    dist[nx][ny][1] = dist[x][y][0]
                    deq.append((nx, ny))
                else:   # map이 1 인 케이스
                    if dist[x][y][1] == 1:
                        dist[nx][ny][0] = dist[x][y][0] + 1
                        dist[nx][ny][1] = dist[x][y][1] - 1
                        deq.append((nx, ny))
    return dist

def solve(n: int, m: int, maps: list[str]) -> None:
    dist = bfs(n, m, maps)

    return dist[n - 1][m - 1][0]


def main() -> None:
    N, M = map(int, sys_input().split())
    maps = [sys_input() for _ in range(N)]
    answer: int = solve(N, M, maps)
    print(answer)

        


if __name__ == '__main__':
    main()