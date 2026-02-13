# Authored by : 21011645
# https://www.acmicpc.net/problem/9498
import sys
input = sys.stdin.readline

score = int(input())

if 90 <= score <= 100:
  print('A')
elif 80 <= score <= 89:
  print('B')
elif 70 <= score <= 79:
  print('C')
elif 60 <= score <= 69:
  print('D')
else:
  print('F')