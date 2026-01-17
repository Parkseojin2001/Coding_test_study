# Authored by : 21011645
# https://www.acmicpc.net/problem/1406

import sys
input = sys.stdin.readline

class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.prev = prev
        self.next = next

head = ListNode("head", None, None)
tail = ListNode("tail", None, None)

head.next = tail
tail.prev = head

cur = head

for c in list(input().rstrip()):
    new_node = ListNode(c, None, None)
    
    new_node.prev = cur
    new_node.next = tail
    
    cur.next = new_node
    tail.prev = new_node
    
    cur = new_node

cur = tail
    
for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if cur.prev != head:
            cur = cur.prev
    elif command[0] == 'D':
        if cur != tail:
            cur = cur.next        
    elif command[0] == 'B':
        if cur.prev != head:
            cur.prev.prev.next = cur
            cur.prev = cur.prev.prev
    elif command[0] == 'P':
        new_node = ListNode(command[1], None, None)
        
        new_node.prev = cur.prev
        new_node.next = cur
        
        cur.prev.next = new_node
        cur.prev = new_node
        
cur = head.next

while cur.val != 'tail':
    print(cur.val, end='')
    cur = cur.next
    
        
    
    

