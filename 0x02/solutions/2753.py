# Authored by : 21011645
# https://www.acmicpc.net/problem/2753
import sys
input = sys.stdin.readline
year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
  print(1)
else:
  print(0)
