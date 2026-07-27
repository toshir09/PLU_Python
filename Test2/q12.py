from collections import deque
queue = deque([10, 20, 30, 40])
while queue:
    print(queue.popleft(), end=" ")