from collections import deque
queue = deque([10, 20, 30, 40])
queue.popleft()
print(list(queue))