
class TreeNode:
    def __init__(self):
        self.left = None # 왼쪽 자식 노드
        self.data = None # 노드에 저장될 데이터
        self.right = None # 오른쪽 자식 노드

def pre_order(node):
    if node is None:
        return
    print(node.data, end = '->')
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if node is None:
        return
    pre_order(node.left)
    print(node.data, end='->')
    pre_order(node.right)

def post_order(node): # 후위 순회 (L R P)
    if node is None:
        return
    post_order(node.left) # 왼쪽 서브트리 순회
    post_order(node.right) # 오른쪽 서브트리 순회
    print(node.data, end ='->') # 현재 노드 출력

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

# search 함수
def search(find_number):

    current = root
    while True:
        if find_number == current.data:
            return True

        elif find_number < current.data:
            if current.left is None:
                return False
            current = current.left

        else:
            if current.right is None:
                return False
            current = current.right

def delete(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)

    else:  # 삭제할 노드 발견
       # 자식이 없는 leaf 노드거나 자식이 하나만 있는 경우
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        # 자식이 둘 다 있는 경우: 오른쪽 서브트리의 최솟값으로 대체
        min_larger_node = node.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left # move

        node.data = min_larger_node.data  # 값 복사
        node.right = delete(node.right, min_larger_node.data)  # 오른쪽 서브트리에서 중복값 제거

    return node


if __name__ == "__main__":
    numbers = [10,15,8,3,9,14]  # 삽입할 숫자 리스트
    root = None # 초기 루트는 None

    # 리스트의 숫자들을 하나씩 BST에 삽입
    for number in numbers:
        root  = insert(root, number)

    print("BST 구성완료")
    post_order(root) # 후위 순회 결과 출력
    print()
    in_order(root) # 중위 순회 결과 출력
    print()
    pre_order(root) # 전위 순회 결과 출력
    print()

    number = int(input("찾고자 하는 값: "))

    if search(number): # search 함수에 입력 부분 제거, 출력 부분 제거, 함수의 매개변수는 찾고자 하는 값, 리턴 값은 bool
        print(f"{number}을(를) 찾았습니다")
    else:
        print(f"{number}이(가) 존재하지 않습니다")

    # 삭제
    del_number = int(input("제거 하는 값: "))
    root = delete(root, del_number)
    post_order(root) # 후위 순회 결과 출력
    print()
    in_order(root) # 중위 순회 결과 출력
    print()
    pre_order(root) # 전위 순회 결과 출력
    print()




