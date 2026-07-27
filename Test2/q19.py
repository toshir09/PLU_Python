from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
visited = set()
queue = deque(['A'])
while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in graph[node]:
            if i not in visited:
                queue.append(i)