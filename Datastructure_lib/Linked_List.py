class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        
class linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):             # 노드 추가 함수 [뒤]
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def prepend(self, data):            # 노드 추가 함수 [앞]
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node

    def delete(self, data):             # 노드 삭제 함수
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def get(self, index):
        return self.__getitem__(index)

    def display(self):                  # 노드 상태 출력 함수
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    def count_nodes(self):              # 노드 갯수 세는 함수
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        if index < 0:
            # 음수 인덱스 처리
            index = len(self) + index
            
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        return current.data

    def __setitem__(self, index, data):
        if index < 0:
            # 음수 인덱스 처리
            index = len(self) + index
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        current.data = data