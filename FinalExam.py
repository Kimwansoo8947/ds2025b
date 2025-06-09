
class Graph:
    def __init__(self, size):
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print(' ', end = ' ')
    for v in range(len(g.graph)):
        print(name_ary[v], end = ' ')

    for row in range(len(g.graph)):
        print(name_ary[row], end= ' ')

        for col in range(len(g.graph)):
            print(f"{g.graph[row][col]:2d}", end = ' ')
        print()
    print()


# dfs => 재귐함수
def dfs(g, current, visited):
    visited.append(current)

    for vertex in range(graph_size):
        if g.graph[current][vertex] > 0 and vertex not in visited:
            dfs(g,vertex, visited)


def find_vertex(g, find_vtx):
    visited_ary = list()
    start = 0
    dfs(g, start, visited_ary)
    return find_vtx in visited_ary


g1 = None
name_ary = ['인천', '서울', '강릉', '대전', '광주', '부산']
Incheon, seoul, gangneung, daejeon, gwangju, busan = 0, 1, 2, 3, 4, 5


graph_size = 6
g1 = Graph(graph_size) # 6행 6열짜리
g1.graph[Incheon][seoul] = 10; g1.graph[Incheon][gangneung] = 15
g1.graph[seoul][Incheon] = 10; g1.graph[seoul][gangneung] = 40; g1.graph[seoul][daejeon] = 11; g1.graph[seoul][gwangju] = 55
g1.graph[gangneung][Incheon] = 15; g1.graph[gangneung][seoul] = 40; g1.graph[gangneung][daejeon] = 12
g1.graph[daejeon][seoul] = 11; g1.graph[daejeon][gangneung] = 12; g1.graph[daejeon][gwangju] = 20; g1.graph[daejeon][busan] = 30
g1.graph[gwangju][seoul] = 55; g1.graph[gwangju][daejeon] = 20; g1.graph[gwangju][busan] = 28
g1.graph[busan][daejeon] = 30; g1.graph[busan][gwangju] = 28


print("도시 간 도로 건설을 위한 전체 연결도")
print_graph(g1)

edge_ary = []

for i in range(graph_size):
    for j in range(graph_size):
        if g1.graph[i][j] !=0:
            edge_ary.append([g1.graph[i][j],i,j])

print(edge_ary)

# 가중치 기준으로 내림차순 정렬
edge_ary.sort(reverse=True)
print(edge_ary)

# 중복 간선 제거
new_ary = []
for i in range(1, len(edge_ary),2):
    new_ary.append(edge_ary[i])
print(new_ary)

index = 0

while len(new_ary) > graph_size -1:
    # 백업
    start = new_ary[index][1]
    end = new_ary[index][2]
    save_cost = new_ary[index][0]

    # 무방향 그래프
    g1.graph[start][end] = 0
    g1.graph[end][start] = 0

    start_reachable = find_vertex(g1, start)
    end_reachable = find_vertex(g1, end)

    if start_reachable and end_reachable:
        del new_ary[index]

    else:
        g1.graph[start][end] =save_cost
        g1.graph[end][start] = save_cost
        index = index + 1

print("최소 비용 계산")
print_graph(g1)

total_cost = 0

for i in range(graph_size):
    for j in range(graph_size):
        if g1.graph[i][j] !=0:
            total_cost = total_cost + g1.graph[i][j]

total_cost = total_cost // 2
print(f"최소 비용의 도로 건설 비용: {total_cost}")