# BST 이진 탐색 트리

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def pre_order(node): # P L R
    if node is None:
        return

    print(node.data , end = '->')
    pre_order(node.left)
    pre_order(node.right)

def in_order(node): # L P R
    if node is None:
        return

    in_order(node.left)
    print(node.data, end = '->')
    in_order(node.right)


def post_order(node): # L R P
    if node is None:
        return

    post_order(node.left)
    post_order(node.right)
    print(node.data, end = '->')


# 삽입
def insert(root, value):

    new_node = TreeNode()
    new_node.data = value

    if root is None:
        return new_node

    current = root

    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break

            current = current.left

        else:
            if current.right is None:
                current.right = new_node
                break

            current = current.right


    return root

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
                return  False
            current = current.right

def delete(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        min_larger_node = node.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        node.data = min_larger_node.data
        node.right = delete(node.right, min_larger_node.data)

    return node


if __name__ == "__main__":
    numbers = [10,15,8,3,9,14]
    root = None

    for number in numbers:
       root = insert(root, number)


    print("BST 구성 완료")
    post_order(root)
    print()
    in_order(root)
    print()
    pre_order(root)
    print()

    number = int(input("찾고자 하는 값: "))

    if search(number):
        print(f"{number}을 찾았습니다.")
    else:
        print(f"{number}이(가) 존재하지 않습니다.")

    del_number = int(input("제거하는 값: "))
    root = delete(root, del_number)
    post_order(root)
    print()
    in_order(root)
    print()
    pre_order(root)
    print()