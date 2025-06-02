class Graph:
	def __init__ (self, size):
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

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

def find_vertex(g, find_vtx) : # 깊이 우선 탐색 재귀나 스택 사용 여기서는 스택 사용
	stack = list()
	visited_ary = list()

	current = 0	# 시작 정점
	stack.append(current)
	visited_ary.append(current)

	while stack: # 스택 안에 뭐가 있을떄까지
		next = None
		for vertex in range(graph_size):
			if g.graph[current][vertex] != 0:  # 연결되어 있으면 => 2차원 현재 행과 정점
				if vertex in visited_ary:	# 방문한 적이 있는 정점
					pass
				else :			# 방문한 적이 없으면
					next = vertex  #  다음 정점으로 지정 (다음 열로 이동)
					break

		if next is not None:				# 다음에 방문할 정점이 있는 경우
			current = next
			stack.append(current)  # push
			visited_ary.append(current)  # push (어디 방문 했는지 순서 기록)
		else :					# 다음에 방문할 정점이 없는 경우
			current = stack.pop() # 방문 할 떄가 없으면 되돌아옴

	if find_vtx in visited_ary: #visited_ary에 내가 찾은 값이 있으면 (도시가 연결되어 있는지)
		return True
	else :
		return False

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

edge_ary.sort(reverse=True) # 원본을 가중치 기준으로 내림차순으로 정렬
print(edge_ary)

new_ary = list()
for i in range(1, len(edge_ary), 2): # 1,3,5,7 ... 2씩 증가
	new_ary.append(edge_ary[i])
print(new_ary)

index = 0
while len(new_ary) > graph_size - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복
    # 백업 (3줄)
	start = new_ary[index][1] # new_ary (간선) 출발도시
	end = new_ary[index][2] # 도착도시
	save_cost = new_ary[index][0] # 가중치

    # 시작도시 도착 도시 0으로 초기화
	g1.graph[start][end] = 0
	g1.graph[end][start] = 0

    # 그래프가 삭제된 후 연결이 되어 있는지 확인하는 find_vertex 함수 호출
	start_reachable = find_vertex(g1, start)
	end_reachable = find_vertex(g1, end)


	if start_reachable and end_reachable :
		del new_ary[index] # 삭제
	else:
        # 백업해 놓은거 복원
		g1.graph[start][end] = save_cost
		g1.graph[end][start] = save_cost
		index = index + 1 # 인덱스 증가 (끝내야 함)  (중요)

print('최소 비용의 계산')
print_graph(g1)

total_cost = 0
for i in range(graph_size):
	for k in range(graph_size):
		if g1.graph[i][k] != 0:
			total_cost = total_cost + g1.graph[i][k]

total_cost = total_cost // 2 # 무방향 그래프니까 절반은 날려야함
print(f"최소 비용의 도로 건설 비용 :  {total_cost}")