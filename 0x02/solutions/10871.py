# Authored by : 21011645
# https://www.acmicpc.net/problem/10871
import sys
input = sys.stdin.readline

N, X = map(int, input().split())

A = list(input().split())

for i in range(N):
  if int(A[i]) < X:
    print(A[i], end=' ')