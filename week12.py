from  collections import  deque
# 깊이 우선 탐색 DFS
# 0 == A, 1==B, 2==C, 3==D, 4 = E, 5 = F, 6 = G , 7 = H
graph = [
    [0, 1 ,1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i , visited):
    visited[i] =1
    print(chr(ord('A')+i), end = ' ')
    for j in range(len(g)):
        if g[i][j] ==1 and not visited[j]:
            dfs(g,j,visited) # 재귀 함수

# BFS 깊이 우선 탐색
def bfs(g,i, visited):
    queue = deque([i]) # popleft, append # i값 넣고 시작함
    visited[i] = True # i 값 방문 처리
    while queue: # 큐안에 값이 존재할떄까지 (방문할 노드가 남아있다는 뜻)
        # print(visited)
        i = queue.popleft() # dequeue외 같음
        print(chr(ord('A') + i), end=' ')
        for j in range(len(g)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j) # 큐애서 삽입
                visited[j] = True # 방문처리

# visited_dfs는 각 노드가 방문되었는지 기록하는 리스트 (0 = 미방문, 1 = 방문함)
visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [False for _ in range(len(graph))]

# DFS 시작 (0번 노드, 즉 'A'부터 탐색 시작)
dfs(graph,6,visited_dfs)
print()
bfs(graph,1,visited_bfs)

