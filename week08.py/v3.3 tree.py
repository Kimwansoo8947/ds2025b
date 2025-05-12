class TreeNode:
    def __init__(self):
        self.left = None # 왼쪽 자식 노드
        self.data = None # 노드에 저장될 데이터
        self.right = None # 오른쪽 자식 노드

def post_order(node): # 후위 순회 (L R P)
    if node is None:
        return
    post_order(node.left) # 왼쪽 서브트리 순회
    post_order(node.right) # 오른쪽 서브트리 순회
    print(node.data, end =' ') # 현재 노드 출력

# BST에 값을 삽입하는 함수
def insert(root, value):
    new_node = TreeNode() # 새 노드 생성
    new_node.data = value # 새 노드에 값 설정

    if root is None: # 첫번 째 노드일 때 처리
        return new_node

    current = root # 현재 노드애서 탐색 시잗

    while True:
        if value < current.data: # 왼쪽으로 가야 하는 경우
            if current.left is None: # 왼쪽 자식이 비어 있으면 삽입
                current.left = new_node
                break

            current = current.left # move (더 왼쪽으로 이동)
        else: # 오른쪽으로 가야 하는 경우
            if current.right is None: # 오른쪽 자식이 비어 있으면 삽입
                current.right = new_node
                break

            current = current.right # move (더 오른 쪽으로 이동)

    return root # 루트 노트를 반환



if __name__ == "__main__":
    numbers = [10,15,8,3,9]  # 삽입할 숫자 리스트
    root = None # 초기 루트는 None

    # 리스트의 숫자들을 하나씩 BST에 삽입
    for number in numbers:
        root  = insert(root, number)

    print("BST 구성완료")
    post_order(root) # 후위 순회 결과 출력
