class Node:
    def __init__(self, data, link = None):
        self.data =data
        self.link = link

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def enqueue(self, data):
        # 삽입이 되면 사이즈  1 증가
        self.size = self.size + 1
        node = Node(data)
        if self.rear is None:  # 아무것도 없음
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node


q = Queue()
q.enqueue("Database")
q.enqueue("Data structure")
print(q.size, q.front.data, q.rear.data)



