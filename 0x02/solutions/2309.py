# Authored by : 21011645
# https://www.acmicpc.net/problem/2309
import sys
input = sys.stdin.readline

heights = []

for _ in range(9):
  heights.append(int(input()))
  
rest = sum(heights) - 100

heights.sort()

left = 0
right = len(heights) - 1

while left < right:
  if heights[left] + heights[right] == rest:
    break
  elif heights[left] + heights[right] < rest:
    left += 1
  else:
    right -= 1
  
for h in heights:
  if h == heights[left] or h == heights[right]:
    continue
  print(h)