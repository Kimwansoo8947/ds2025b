class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Stack:
    def __init__(self):
        # self: 실행시점의 객체
        self.top = None


    def push(self, data):
        node = Node(data)

        if self.top is None:
            self.top= node
        else:
            node.link = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return "Stack is empty!"
        popped_node = self.top
        self.top = self.top.link
        return popped_node.data

s1 = Stack()
print(s1.pop())
s1.push("자료구조")
s1.push("데이터베이스")
print(s1.pop())
print(s1.pop())




