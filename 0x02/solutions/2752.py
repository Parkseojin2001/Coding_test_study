# Authored by : 21011645
# https://www.acmicpc.net/problem/2752
import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[0], numbers[1], numbers[2])

