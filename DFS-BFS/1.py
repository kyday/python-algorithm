# 탐색 ? 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# 대표적으로 DFS / BFS 그래프 탐색 알고리즘이 있다.
# DFS 깊이 우선 탐색



graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보들은 모든 노드를 방문하지 않은 것처럼 처리
visited = [False] * 9

def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  visited[v] = True
  print(v, end=' ')

# 방문하지 않은 1차원 배열에서 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i , visited)

      
dfs(graph,1,visited)