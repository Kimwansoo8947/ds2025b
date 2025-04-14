# 스택
# 스택의 요소를 추적하기 위해 링크드 리스트를 쓸 수도 있고 배열을 쓸 수도 있다.
from traceback import print_tb


# 스택의 요소의 푸시와 팝은 o(1) 상수시간을 따른다. (푸시 -> 삽입, 팝 -> 삭제)

# 배열을 사용하여 내부적으로 데이터를 관리

# class Stack:
#
#     def __init__(self):
#         self.items = []
#
#     def push(self, data):
#         self.items.append(data)
#
#     def pop(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def peek(self):
#         return self.items[-1]
#
# s1 = Stack()
# s2 = Stack()
# print(s1.is_empty())
# s1.push("자료구조")
# print(s1.is_empty())
# print(s2.is_empty())
# s1.push("데이터베이스")
# print(s1.size())
# print(s1.peek())

# 링크드 리스트를 사용해서 Stack 클래스 구현
class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node

        else:
            node.link = self.top #  새 노드의 링크가 기존 top을 가리키게함
            self.top = node # 새 노드를 top으로 설정

    def pop(self):
        if self.top is None:
            return "스택이 비었습니다"

        popped_node = self.top

        self.top = self.top.link # 이전 노드의 링크를 top으로 설정
        popped_node.link = None # ! 링크 해제 코드
        return popped_node.data

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for i in range(3):
    print(stack.pop())


 # 스택을 사용하여 문자열 뒤집기

def reverse_string(a_string):
    stack = []
    string = ""

    for c in a_string:
        stack.append(c)

    for c in a_string:
        string += stack.pop()

    return string

print(reverse_string("Justin Bibber"))

# 스택과 괄호
def check_parentheses(a_string):
    stack = []

    for c in a_string:

        if c == "(":
            stack.append(c)
        if c == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0


class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node= Node(data)

        if self.top is None:
            self.top = node

        else:
            node.link = self.top # 새 노드의 링크가 기존 top을 가리키게함
            self.top = node # 새 노드를 top으로 설정

    def pop(self):

        if self.top is None:
            return "스택이 비었습니다."

        popped_node = self.top
        self.top = self.top.link

        return popped_node.data
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# for i in range(3):
#     print(stack.pop())

# 스택을 사용해 문자열 뒤집기

# def reverse_string(a_string):
#     stack = []
#     string =""
#
#     for c in a_string:
#         stack.append(c)
#     for c in a_string:
#         string += stack.pop()
#
#     return  string
# print(reverse_string("kim"))

# 스택과 괄호

def check_parentheses(expression: str) -> bool:
    stack = []
    for c in expression:
        if c == "(" or c == "{":
            stack.append(c)
        if c == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return False
            else:
                stack.pop()
        elif c == "}":
            if len(stack) == 0 or stack[-1] != "{":
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(check_parentheses("(2+3)"))
print(check_parentheses("(2+(3*9))"))
print(check_parentheses("(2+(3*9)"))  # 스택에 여는 소괄호가 하나 남아 있어서 False
print(check_parentheses(")2+(3*9)("))