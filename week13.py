# 부모가 같지 않을떄만 union 연산을 한다.
class Graph:
	def __init__ (self, size):
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

class DisjointSet: # 크루스컬 알고리즘을 위한 유틸리티 클래스
	def __init__(self, n):
		self.parent = [i for i in range(n)]

	def find(self ,x):
		if self.parent[x] !=x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self,x,y):
		x_root = self.find(x)
		y_root = self.find(y)

		if x_root != y_root: # 같지 않으면
			self.parent[y_root] = x_root # 덮어쓰기
			return True
		return False


def print_graph(g) :
	print(' ', end = ' ')
	for v in range(len(g.graph)) : # ex) 5가오면 5 * 5 = 25
		print(name_ary[v], end =' ') # label
	print()
	for row in range(len(g.graph)) :
		print(name_ary[row], end =' ') # label
		for col in range(len(g.graph)) :
			print(f"{g.graph[row][col]:2d}", end=' ')
		print()
	print()

# def find_vertex(g, find_vtx) : # 깊이 우선 탐색 재귀나 스택 사용 여기서는 스택 사용
# 	stack = list()
# 	visited_ary = list()
#
# 	current = 0	# 시작 정점
# 	stack.append(current)
# 	visited_ary.append(current)
#
# 	while stack: # 스택 안에 뭐가 있을떄까지
# 		next = None
# 		for vertex in range(graph_size):
# 			if g.graph[current][vertex] != 0:  # 연결되어 있으면 => 2차원 현재 행과 정점
# 				if vertex in visited_ary:	# 방문한 적이 있는 정점
# 					pass
# 				else :			# 방문한 적이 없으면
# 					next = vertex  #  다음 정점으로 지정 (다음 열로 이동)
# 					break
#
# 		if next is not None:				# 다음에 방문할 정점이 있는 경우
# 			current = next
# 			stack.append(current)  # push
# 			visited_ary.append(current)  # push (어디 방문 했는지 순서 기록)
# 		else :					# 다음에 방문할 정점이 없는 경우
# 			current = stack.pop() # 방문 할 떄가 없으면 되돌아옴
#
# 	if find_vtx in visited_ary: #visited_ary에 내가 찾은 값이 있으면 (도시가 연결되어 있는지)
# 		return True
# 	else :
# 		return False

# # 재귀함수 이용
# def dfs(g,current, visited):
# 	visited.append(current) # 시작위치 넣고 시작
# 	for vertex in range(graph_size):
# 		if g.graph[current][vertex]  > 0 and vertex not in visited:
# 			dfs(g,vertex, visited)
#
#
# def find_vertex(g, find_vtx):
# 	visited_ary = list()
# 	start = 0
# 	dfs(g,start, visited_ary)
# 	return find_vtx in visited_ary # True or False (내가 찾고자 하는 도시가 있으면 True)

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

print('도시 간 도로 건설을 위한 전체 연결도')
print_graph(g1)

edge_ary = []  # 결과적으로 2d list
for i in range(graph_size) :
	for j in range(graph_size) :
		if g1.graph[i][j] != 0 :
			edge_ary.append([g1.graph[i][j], i, j]) # 시작 도시와 도착 도시 간선을 추가
print(edge_ary)

edge_ary.sort() # 오름차순
print(edge_ary)


ds = DisjointSet(graph_size)
mst_edges = list()
mst_cost = 0

for cost, s, e in edge_ary:
	if ds.union(s,e):
		mst_edges.append((cost, s,e))
		mst_cost = mst_cost + cost

mst_graph = Graph(graph_size)
for cost, s, e in mst_edges:
	# 무방향
	mst_graph.graph[s][e] = cost
	mst_graph.graph[e][s] = cost

print('최소 비용의 계산')
print_graph(mst_graph)

total_cost = 0
for i in range(graph_size):
	for k in range(graph_size):
		if g1.graph[i][k] != 0:
			total_cost = total_cost + g1.graph[i][k]

total_cost = total_cost // 2 # 무방향 그래프니까 절반은 날려야함
print(f"최소 비용의 도로 건설 비용 :  {mst_cost}")