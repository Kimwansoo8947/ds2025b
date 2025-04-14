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

    def deque(self):
        if self.front is None:
            raise IndexError("Queue is empty!")

        # 무언가 큐에 데이터가 있다는 뜻
        self.size = self.size - 1
        temp = self.front
        self.front = self.front.link

        if self.front is None:
            self.rear = None

        return temp.data



q = Queue()
q.enqueue("Database")
q.enqueue("Data structure")
print(q.size, q.front.data, q.rear.data)
q.deque()
q.deque()
print(q.size, q.front, q.rear)


