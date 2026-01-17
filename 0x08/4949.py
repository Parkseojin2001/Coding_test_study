# Authored by : 21011645
# https://www.acmicpc.net/problem/4949

import sys
input = sys.stdin.readline

parentheses = {
    ')' : '(',
    ']' : '['
}


while True:
    stack = []
    is_valid = 'yes'
    S = input().rstrip('\n')
    if S == '.':
        break
    for c in S:
        if c in list(parentheses.values()):
            stack.append(c)
        elif c in list(parentheses.keys()):
            if stack and stack[-1] == parentheses[c]:
                stack.pop()
            else:
                is_valid = 'no'
                break
    
    if stack:
        is_valid = 'no'
        
    print(is_valid)
        
            