import sys
sys.stdin = open('input.txt')

from collections import deque

def traversals(current = 1):

    preorder_traversal.append(inverse_orders[current])
    if adjacency_list[current][0] != chr(46):
        traversals(alphabets_orders[adjacency_list[current][0]])
    inorder_traversal.append(inverse_orders[current])
    if adjacency_list[current][1] != chr(46):
        traversals(alphabets_orders[adjacency_list[current][1]])
    postorder_traversal.append(inverse_orders[current])
    return

# 알파벳과 인덱스를 연동
alphabets_orders = {}
for idx in range(26):
    alphabets_orders[chr(65 + idx)] = idx + 1
inverse_orders = {value: key for key, value in alphabets_orders.items()}

N = int(input())
adjacency_list = [0] * (N + 1)
for _ in range(N):
    idx, *children = input().split()
    adjacency_list[alphabets_orders[idx]] = children

preorder_traversal = deque()
inorder_traversal = deque()
postorder_traversal = deque()

traversals()

print(''.join(preorder_traversal))
print(''.join(inorder_traversal))
print(''.join(postorder_traversal))