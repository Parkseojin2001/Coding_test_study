# Authored by : 21011645
# https://www.acmicpc.net/problem/1406

import sys
input = sys.stdin.readline

left = list(input().rstrip())
right= []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L' and len(left) != 0:
        top = left.pop()
        right.append(top)
    elif command[0] == 'D' and len(right) != 0:
        top = right.pop()
        left.append(top)
    elif command[0] == 'B' and len(left) != 0 :
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))