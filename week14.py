class TreeNode:
    def __init__(self):
        self.right = None
        self.data = None
        self.left = None


def post_order(node):
    if node is None:
        return None
    post_order(node.left)
    post_order(node.right)
    print(node.data, end = '-')

def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:
        return new_node

    current  = root

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

if __name__ == "__main__":
    numbers = [50,30,2,45,28,5,98,52,60]
    root = None

    for number in numbers:
        root = insert(root, number)

    post_order(root)
