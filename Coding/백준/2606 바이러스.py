com = int(input())
con = int(input())

graph = [[] for _ in range(com + 1)]

for i in range(con):
    key, val = map(int, input().split())
    graph[key] += [val]
    graph[val] += [key]

def dfs(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited

result = dfs(graph, 1)

print(len(result) - 1)