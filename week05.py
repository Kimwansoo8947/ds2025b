class Stack:
    def __init__(self):
        # self: 실행시점의 객체
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0 # 비교 연산자 True or False

    def peek(self):
        return self.items[-1]


s1 = Stack()
s2 = Stack()
print(s1.is_empty())

s1.push("자료구조") # s1의 self가 됨
print(s1.is_empty())
print(s2.is_empty())
s1.push("데이터베이스")
print(s1.size())
print(s1.peek()) # 마지막 원소 return만 삭제는 하지 않음 : peek
print(s1.pop())
print(s1.size()) # pop은 삭제 연산이 일어남
print(s1.peek())