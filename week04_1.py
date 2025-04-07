class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        current = self.head

        while current.link is not None:
            current = current.link

        current.link = Node(data)

    def __str__(self):
        node = self.head
        out_txt = ""
        while node is not None:
            out_txt+=f"{node.data}"+" ->"
            node = node.link
        return  out_txt + "end"

    def search(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return f"{target}을 찾았습니다."
            else:
                current = current.link

            return  f"{target}을 찾지 못 했습니다."

    def remove(self, target):
        if self.head.data ==  target:
            self.head = self.head.link
            return

        current = self.head
        previous = None

        while current is not None:
            if current.data == target:
                previous.link = current.link
            previous = current
            current = current.link


    def reverse_list(self):
        current = self.head
        previous = None

        while current:
            link = current.link
            current.link = previous
            previous = current
            current = link
        self.head = previous

a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
a_list.append("Friday")
print(a_list)
print(a_list.search("Tuesday"))
a_list.remove("Tuesday")
print(a_list)