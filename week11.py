# 깊이 우선 탐색 DFS
graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited):
    visited[i] = 1 # i는 방문 노드 번호
    print(chr(ord('A')+i), end = ' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]: # i는 행 j는 열 0을 not 시키면 1 or 1을 not 시키면 0
            dfs(g,j,visited ) # 재귀 함수


def bfs(g,i, visited): # 큐 사용
    pass

visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]

dfs(graph, 0, visited_dfs) # i는 starting point
bfs(graph, 6 , visited_bfs)

# v_dfs = [0,0,0,0,0,0,0,0] # A B C D E F G H
# 방문했던 곳은 return


# BFS 너비 우선 탐색 재귀함수 사용하지 않음
