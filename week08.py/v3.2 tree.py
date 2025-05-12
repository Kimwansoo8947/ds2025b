class TreeNode:
	def __init__(self):
		self.left = None # 왼쪽 자식 노드
		self.data = None # 현재 노드의 값
		self.right = None # 오른쪽 자식 노드


# 메인 실행 부
if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None # 루트 노드 초기화


    # 첫 번째 값을 이용하여 루트 노드 생성
    node = TreeNode()
    node.data = numbers[0]
    root = node


    # 나어지 값들을 순차적으로 BST에 삽입
    for number in numbers[1:]:
        node = TreeNode()
        node.data = number
        current = root

        # 현재 노드부터 시작햐여 적절한 위치에 삽입
        while True:
            if number < current.data:

                # 왼쪽 자식이 없으면 삽입
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # move (왼쪽으로 이동)
            else:

                # 오른쪽 자식이 없으면 삽입
                if current.right is None:
                    current.right = node
                    break
                current = current.right  # move (오른쪽으로 이동)

    print("BST 구성 완료")

    # 사용자로부터 찾을 숫자 입력 받기
    find_number = int(input())

    current = root
    while True:
        if find_number == current.data:
            print(f"{find_number}을(를) 찾았습니다")
            break
        elif find_number < current.data:
            if current.left is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.left  # 왼쪽 서브트리로 이동
        else:
            if current.right is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.right  # 오른쪽 서브트리로 이동
