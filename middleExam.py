# 중간고사 대비 정리
# 시간 복잡도 : n이 커짐에 따라 알고리즘이 실행되고 왼료될 때까지 필요한 단계
# 상수시간  -> 로그시간 -> 선형시간 -> 선형 로그 시간 -> 2차 시간 -> 3차 시간 -> 지수 시간 -> 팩토리얼

# 상수시간 O(1)
# 입력 데이타의 크기에 상관 없이 언제나 일정한 시간이 걸림
# 데이터 세트가 아무리 커지더라도 알고리즘 실행시간이 변하지 않으므로 가장 효율적이다.

# 로그시간 (0 log n)
# 상수 시간에 이어 두 번째로 효율적인 시간 복잡도
# 실행을 반복할 때 마다 알고리즘의 탐색 범위를 1/2로 줄여 나감
# 데이터 세트가 커짐에 따라 알고리즘의 실행에 필요한 단계가 천천히 늘어나는 알고리즘
# ex) n = 16일 경우 실행 단계는 4
# 개수가 증가 할떼 시간(단계)는 덜 증가하는 경우의 표기

# 선형 시간 0(n)
# 선형 시간으로 실행되는 알고리즘은 데이터 크기가 커지는 만큼 갈은 비율로 단계가 늘어나는 알고리즘
# 문제 해결에 필요한 단계가 입력값(n)과 1:1 관계를 가짐
# 데이터 세트가 커지는 만큼 단계도 같은 비율로 늘어남

n = int(input("정수 입력: "))
result = 0
# for i in range(1, n+1):
#     result = result + i # 선형시간 o(n)

result = n * (n+1) //2 # 상수 시간 o(1)
print(result)

# 선형 로그 시간 o(n log n)
# 로그 시간 복잡도와 선형 시간 복잡도를 곱한 만큼 커진다.
# 입력 값이 증가 할때 시간 (단계)를 더 증가하는 경우
# 선형 로그 시간은 선형 시간 복잡도 보다 비효율적이지만 2차 시간 복잡도 보다는 효율적이다.

# 2차 시간
# 2차 시간으로 실행되는 알고리즘의 복잡도는 n의 제곱에 정비례하며 o(n**2)으로 표기한다.
# 문제 해결에 필요한 단계가 입력 값 (n)의 제곱 만큼 수행된다.

# 3차 시간
# 알고리즘의 시간 복잡도는 n의 세제곱에 정비례하며 O(n**3)으로 표기한다.

# 지수 시간

# 최선과 최악
# 최선의 경우인 시간 복잡도는 알고리즘에 입력되는 데이터가 이상적일때
# 최악의 경우인 시간 복잡도는 말 그대로 가능한 모든 시나리오 중 가장 최악(알고리즘의 실행 시간이 급격하게 커지는 / 느려지는 경우)일때
# 평균의 경우인 시간 복잡도는 알고리즘이 평균적으로 얼마나 빨리 실행되는지를 나타낸다.

# 공간 복잡도 (메모리를 얼마나 차지하는지)
# 공간 복잡도는 알고리즘의 실행을 완료할 때까지 필요한 자원의 양, 즉 고정 공간, 데이터 구조 공간, 임시 공간의 메모리를 얼마나 사용하는지 나타낸다.
# 일반적으로 공간을 적게 사용하는 것이 좋다.


import  random


# 알고리즘 분석
n = int(input("정수 입력: "))
result = 0

for i in range(1, n+1):
    result = result + i  # 시간 복잡도 선형시간

result = n*(n+1)//2 # O(1) 상수시간
print(result)

# Guess Game
# answer = random.randint(1,100)
# win = False
#
# for guess in range(7):
#     print(f"{7-guess}번의 기회가 남았습니다. 숫자 입력: ", end = "")
#     guess = int(input()) #  숫자 입력
#
#     if answer == guess:
#         print("정답입니다.")
#         win = True
#         break
#     elif answer > guess:
#         print("입력하신 수는 정답보다 작은 수 입니다. LOW")
#     else:
#         print("입력하신 수는 정답보다 큰 수 입니다. HIGH")
# if win:
#     print("You Win!")
# else:
#     print(f"You lose. The answer is {answer}.")


# 배열
# 연속적인 메모리 블록에 인덱스와 함께 요소를 저장하는 자료구조이다.
# 정적 자료구조는 일단 생성하면 크기를 바꿀 수 없는 자료구조
# 배열에 저장된 각 요소는 인덱스를 통해 접근 할 수 있다.
# 배열의 첫번째 요소가 저장된 메모리 위치를 시작주소라고 합니다.

# 1차원 배열
array = [1,2,3]
print(array[0])

# 2차원 배열
multi_array = [[1,2,3],[4,5,6],[7,8,9]]
print(multi_array[1][2])

# 배열의 성능
# 배열은 요소에 접근하고 수정하는 작업은 상수시간을 따른다.
# 다만 정렬되지 않은 배열을 탐색할 때는 요소 전체를 순회하므로 선형시간을 따른다.
# 배열의 개별 요소에 접근하거나 수정하는 것은 대단히 빠른 것은 맞지만 추가나 삭제등 어떤 향태로든 배열을 변경하는 작업은 선형시간을 따른다.
# 따라서 배열에 요소를 추가하는 작업은 선형시간을 따르기 때문에 거대한 데이터 세트에 자주 데이터를 추가해야 한다면 배열이 최선의 선택이 될 수 없다.

array = [11,9,-77,8]
for i in range(len(array)):
    print(f"{array[i]:3} {id(array[i])}")

import array
arr = array.array('f',[11,9,-77,8])

for i in range(len(arr)):
    print(f"{arr[i]:3} {id(arr[i])}")

# 0 옮기기
def move_zeros(l):
    zeroIndex = 0
    for i, v in enumerate(l): # enumerate: 인덱스 번호, 값 동시 리턴
        if v !=0: # 현재 값이 0이 아니라면
            l[zeroIndex] = v # zeroIndex 위치에 현재 숫자 저장

            if zeroIndex != i: # zeroIndex와 index와 일치 하는지 확인
                l[i] = 0 # 일치하지 않는다면 index 위치에 있는 값 0으로 변경
            zeroIndex+=1 # zeriIndex는 1을 더함

    return (l)

# enumerate 사용하지 않고 0 옮기기
def move_zero(a_list):
    zeroIndex = 0
    for i in range(len(a_list)):
        v = a_list[i]

        if v !=0:
            a_list[zeroIndex] =v

            if zeroIndex != i:
                a_list[i] = 0
            zeroIndex+=1
    return (a_list)


l = [11,0,9,0,-77]
move_zeros(l)
print(l)

a_list = [11,0,9,0,-77]
move_zeros(a_list)
print(a_list)

# 리스트 결합
# 튜플은 값을 추가 또는 삭제 할 수 없는 불변의 자료구조

groups = ['HOT','Seventeen','Black Pink','NJZ']

#ratings = [1,2,4,3,100]
ratings = [1,2,4,3]
print(list(zip(groups,ratings)))

# 중복 요소 찾기 (set()은 중복을 허용하지 않음)
# 세트의 중복 요소 찾기
# 세트는 중복을 허용하지 않기 때문에 이터러블 (순환하는) 데이터에서 요소를 하나씩 추가할때, 세트의 길이가 그래로라면 추가할때, 요소가 중복이라는 것을 알수 있다.

city = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
city = set(city)
print(city) # 딕셔너리로 출력됨

def duplicate_city(cities):
    result = list() # 중복된 요소를 담을 리스트
    s =set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 =len(s)

        if l1 == l2: # 중복된 값
            result.append(city)


    return result


cities = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
cities.append('Anyang')
cities.append('Seoul')
print(cities)
print(set(duplicate_city(cities)))

def intersection(l1,l2):
    l3 = list() # 리스트로 변환
    for v in l1:
        if v in l2:
            l3.append(v) # 교집합 리스트에 추가
    return l3

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
print(intersection(l1, l2))

def intersection2(l1,l2):

    l3 =[v for v in l1 if v in l2] # 리스트 컴프리핸션 (리스트 축약) 사용
    return l3

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
print(intersection2(l1, l2))

# 세트를 사용하여 교집합 찾기
# 세트에는 모두 존재하는 요소를 반환하는 교집합 함수 intersection이 있다.
def inters(l1,l2):
    s1 =set(l1)
    s2 =set(l2)

    return list(s1 & s2) # 리스트로 변환.
    # return list(s1.intersection(s2))
l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
print(inters(l1,l2))
# 배열 연습문제
# 음이 아닌 정수로 구성되어 있는 an_array에서 짝수만 추출한 배열과 홀수만 추출한 배열을 만들어보시오.

# an_array = [10,2,5,9,4]
# arr1 = []
# arr2 = []
#
# for i in range (len(an_array)):
#     if an_array[i] %2 ==0:
#         arr1.append(an_array[i])
#     else:
#         arr2.append(an_array[i])
#
# print(arr1)
# print(arr2)

# 링크드 리스트
# 배열과 마찬가지로 앞이나 뒤에 요소 추가하고 탐색하며 삭제할 수 있다.
# 하지만 링크드 리스트는 인덱스가 없다.
# 링크드 리스트의 요소는 연속적인 메모리 블록에 저장하지 않는다.
# 링크드 리스트는 데이터를 보관하는 필드와 다음 노드의 위치를 나타내는 포인터로 이루어짐
# 링크드 리스트의 첫번쩨 노드는 헤드라고 부른다.
# 마지막 노드에는 None을 가리키는 포인터가 포함되므로 이를 확인하면 해당 리스트의 마지막 노드임을 알수있다.
# 링크드 리스트는 배열과 달리 비연속적인 메모리에도 저장할 수 있다.
# 링크드 리스트에는 요소를 삽입해도 다른 데이터를 밀어낼 필요가 없다.
# 링크드 리스트는 삽입 삭제는 시간 복잡도가 상수시간이다.
# 단점 반드시 각 노드에 다음 노드를 가리키는 포인터가 있어야 한다. 역시 리소스가 필요하므로 링크드 리스트가 배열보다 더 많은 메모리 사용한다.
# 두번째 단점은 임의 접근이 블가능하다. (링크드 리스트 인덱스 개념이 없다.)
# ex) 배열에서는 언제든 세 번째 요소에 접근할 수 있지만 링크드 리스트에서는 불가능하다.

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 새로운 노드 추가
    def append(self, data):
        if not self.head: # 링크드 리스트가 하나도 없는 상태
            self.head = Node(data) # 새노드를 head에 연결
            return

        current = self.head
        while current.link: # 마지막 노드를 찾을 때 까지
            current = current.link # 다음 노드로 이동

        current.link  = Node(data) #새로운 노드를 마지막 노드에 연결

    # 출력
    def __str__(self):
        node = self.head  # 첫번째 노드를 가리키고 있다.
        out_texts = ""

        while node is not None: # node가 None이 아닐때 까지 반복
            #print(node.data)
            out_texts += f"{node.data} -> "
            # out_texts += str(node.data) + "->"
            node = node.link # node가 가리키고 있는 다음노드를 가져와 node 변수에 저장
        return out_texts + "end"

    # 링크드 리스트 탐색
    def search(self, target):
        current = self.head # 첫번째 노드를 가리키는 head에서 탐색 시작
        while current:
            if current.data == target: # 현재 노드의 데이터가 찾고자 하는 값과 일치하면
                return f"{target}을(를) 찾았습니다."
            else:
                current = current.link # 현재 노드를 다음 노드로 이동

        return f"{target}을(를) 링크드리스트 안에 존재하지 않습니다." # 마지막까지 진행하고 일치하는 요소를 발견하지 못하면 False


    # 링크드 리스트에서 노드 제거
    def remove(self, target):
        current = self.head
        if self.head.data == target: # 첫번째 노드가 삭제 대상일 경우
            self.head = self.head.link # head를 다음노드로 변경
            current.link = None
        return

        previous  = None # 현재 노드의 이전 노드를 저장한 변수

        while current:
            if current.data == target: # 삭제할 노드를 찾으면
                previous.link = current.link # 이전 노드가 현재 노드의 다음 노드를 가리키게 변경
                current.link = None
                break

            previous = current # 현재 노드를 이전 노드에 저장
            current = current.link # 다음 노드로 이동



ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)

for _ in range(20):
    ll.append(random.randint(1,30))

print(ll)
print(ll.search(100))
print(ll.search(10))
print(ll.search(-9))
ll.remove(90)
ll.remove(-9)
ll.remove(10)
ll.remove(8)
print(ll)

# 스택
# 스택에서 요소의 푸시와 팝은 상수시간을 가진다.
# 스택의 요소를 추적하기 위해 링크드 리스트를 쓸 수도 있고, 배열을 사용할 수 도 있다.
# 푸시: 스택에 요소를 추가하는 것
# 팝: 스택에 요소를 꺼내는 것
# 픽 : 스택에 마지막에 있는 요소를 제거하지 않고 접근만 하는 동작
# 스택에 전체 요소를 접근하는 동작은 선형사간을 따르므로 지속적으로 접근해야 하는 알고라즘에는 좋은 선택이 될 수 없다.

# 배열로 스택 만들기

class Stack:

    def __init__(self):
        self.items = list() # 비어 있는 리스트로 초기화

    def push(self, data):
        self.items.append(data) # 새로운 데이터 추가

    def pop(self):
        return self.items.pop() # 가장 최근에 추가된 요소 반환

    def size(self):
        return len(self.items) # 스택의 길이 반환

    def is_empty(self):
        return len(self.items) == 0 # 스택이 비어 있는지 확인

    def peek(self):
        return self.items[-1] # 스택의 마지막, 가장 최근에 추가된 요소를 반환한다.

s1 = Stack()
s2 = Stack()
print(s1.is_empty()) # True
s1.push("자료구조")
print(s1.is_empty()) # False
s1.push("데이터베이스")
print(s1.size())
print(s1.peek())
print(s1.size())
print(s1.pop())
print(s1.size())
print(s1.peek())

# 링크드 리스트를 이용하여 스택 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        node = Node(data)

        if self.top is None: # 링크드 리스트에 head가 없다면
            self.top = node # 새로 만든 노드의 링크가 현재 top을 가리키게 한다.

        else:
            node.link = self.top # 새노드의 링크가 top을 가리키게함
            self.top = node # 스택의 top을 새 노드로 변경

    def pop(self):
        if self.top is None: # 스택이 비어있는 상태
            return "Stack is empty!"

        poppednode = self.top # 현재 top 노드를 임시 저장
        self.top = self.top.link # 현재 top의 바로 아래 노드를 top으로 설정
        poppednode.link = None # 수정

        return poppednode.data # 제거한 노드의 데이터 반환

s1 =Stack()
# print(s1.pop()) #Stack is empty!
s1.push("Data structure")
s1.push("Database")
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())''
for i in range(3):
    print(s1.pop())

# 파이썬 리스트 사용하여 스택 만들기
# pop 메서드는 리스트에서 요소를 제거하며 제거할 요소를 지정하지 않으면 마지막 요소를 제거한다.
stack = []
print(stack)
stack.append('Kanye West')
print(stack)
stack.append('Jay - Z')
print(stack)
stack.append('Chance the Rapper')
print(stack)
stack.pop()
print(stack)

# 스택을 사용하여 문자열 뒤집기

def reverse_string(a_string):
    stack = []
    string = ""
    for c in a_string:
        stack.append(c)

    for c in a_string:
        string += stack.pop()
    return string
print(reverse_string("Bibber"))

# 스택과 괄호
def check_parentheses(expression:str) -> bool:
    stack = []
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0

print(check_parentheses("(2+3)"))
print(check_parentheses("(2+(3*9))"))
print(check_parentheses("(2+(3*9)")) # 스택에 여는 소괄호가 하나 남아 있어서 False
print(check_parentheses(")2+(3*9)("))

# 괄호의 짝이 맞는지 확인하는 프로그램을 확장해 중괄호 {}의 짝도 확인할 수 있는 프로그램을 만드시오.

def check_parentheses2(expression :str) -> bool:
    stack = []

    for letter in expression:
        if letter == "(" or letter == "{":
            stack.append(letter)
            
        elif letter == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return False
            else:
                stack.pop()

        elif letter == "}":
            if len(stack) == 0 or stack[-1] != "{":
                return False
            else:
                stack.pop()

    return len(stack) == 0

# 큐
# 뒤애서 요소를 추가하고 앞에서부터 요소를 꺼내는 선형 자료구조
# 큐는 대표적으로 FIFO 선입선출 자료구조이다.
# 인큐는 요소를 큐에 추가하는 과정이고 디큐는 요소를 큐에서 제거하는 과정이다.
# 인큐는 큐의 뒷부분에서 요소를 추가하고 디큐는 큐의 앞부분에서 요소를 제거한다.
# 제한적 큐: 추가할 수 있는 요소의 수에 제한이 있는 큐
# 무제한 큐: 추가할 수 있는 요소의 수에 제한이 없는 큐
# 인큐와 디큐는 모두 큐의 크기에 상관 없이 o(1) 상수시간을 따른다.
# 큐에 있는 요소에 접근하고 탐색하는 작업은 o(n) 선형시간을 따른다.
# 큐는 순서대로 입출력하는 상황에 이상적인 자료구조이다.

# 링크드 리스트를 사용해 큐 구현

class Node:
    def __init__(self, data, link =None):
        self.data = data
        self.link = link

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        self.size  = self.size +1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError ("Queue is empty!")

        temp = self.front
        self.front = self.front.link

        if self.front is None:
            self.reat = None
        temp.link = None

        return temp.data


q = Queue()
q.enqueue("Database")
q.enqueue("Data structure")
print(q.size, q.front.data, q.rear.data)
q.dequeue()
q.dequeue()
print(q.size, q.front, q.rear)

# 파이썬에 내장된 큐 클래스
from queue import Queue
q = Queue()
q.put("Database")
q.put("Data structure")
print(q.get())
print(q.get())
