# Authored by : 21011645
# https://www.acmicpc.net/problem/7576
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

tomatoes = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if tomatoes[ny][nx] == 0:
                    tomatoes[ny][nx] = tomatoes[y][x] + 1
                    queue.append((ny, nx))
    

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j))

bfs()

days = 0

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            print(-1)
            exit()
        days = max(days, tomatoes[i][j])


print(days - 1)