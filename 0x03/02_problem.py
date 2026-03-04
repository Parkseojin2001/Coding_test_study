# Authored by : 21011645
# https://www.acmicpc.net/problem/10808
import sys

input = sys.stdin.readline

S = input().strip()

count = [0] * 26
list_s = list(S)
# ASCII CODE
for c in list_s:
    num = ord(c) - ord("a")
    count[num] += 1


for c in count:
    print(c, end=" ")
