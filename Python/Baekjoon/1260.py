from collections import deque
import sys 
input = sys.stdin.readline

def dfs(num):
    dfs_visited[num] = True
    print(num, end=" ")
    for i in sorted_graph[num]:
        if dfs_visited[i] == False:
            dfs(i)


def bfs(num):
    queue = deque([num])
    bfs_visited[num] = True
    while queue:
        vertex = queue.popleft()
        print(vertex, end =" ")
        for i in sorted_graph[vertex]:
            if bfs_visited[i] == False:
                queue.append(i)
                bfs_visited[i] = True


N, M, V = map(int, input().split())

dfs_visited = [False]*(N+1)
bfs_visited = [False for _ in range(N+1)]

graph =[[] for _ in range(N+1)]

for _ in range(1,M+1):
    node_A , node_B = map(int, input().split())
    graph[node_A].append(node_B)
    graph[node_B].append(node_A)

sorted_graph = []
for i in graph:
    sorted_graph.append(sorted(i))

dfs(V)
print()
bfs(V)