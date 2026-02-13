# Authored by : 21011645
# https://www.acmicpc.net/problem/2480
import sys
input = sys.stdin.readline

dice = list(map(int, input().split()))

if len(set(dice)) == 1:
  print(10000 + dice[0] * 1000)
elif len(set(dice)) == 2:
  print(1000 + 100 * (sum(dice) - min(dice) - max(dice)))
else:
  print(max(dice) * 100)
  