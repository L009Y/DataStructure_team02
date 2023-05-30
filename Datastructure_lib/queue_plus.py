class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List_Queue:
    def __init__(self):
        self.length = 0
        self.head = None    # 나가는 곳
        self.tail = None    # 들어오는 곳
        
    def IsEmpty(self):
        if self.head is None:
            return True
        return False
        
    def enqueue(self, data):        # tail에 data 삽입 함수
        temp_Node = Node(data)
        
        if self.head is None:       # 비어 있을 경우, head와 tail에 새 노드 추가
            self.head = temp_Node
            self.tail = temp_Node
        else:                       # 비어 있지 않을 경우 (데이터 존재), tail의 next에 새 노드 할당 -> tail에 next 할당
            self.tail.next = temp_Node
            self.tail = self.tail.next
        self.length += 1
            
    def dequeue(self):              # head에서 data 출력 함수
        d_value = None
        if self.IsEmpty is True:    # 비어 있을 경우, print
            print("Queue Empty")
        else:                       # 비어 있지 않을 경우, value에 head의 data 할당 -> head를 기존 head의 next로 변경
            d_value = self.head.data
            self.head = self.head.next
            
        if self.head is None:
            self.tail = None
        
        self.length -= 1
        return d_value
    
    def peek(self):                 # head의 값을 꺼내지 않고 data 확인 함수
        p_value = None
        if self.IsEmpty is True:
            print("Queue Empty")
        else:
            p_value = self.head.data
        
        return p_value
    
    def find_None(self, data):      # 입력 data를 찾고, 찾으면 data를 -1 할당, 아니면 그대로 두는 함수
        temp_Node = self.head
        
        if self.IsEmpty is True:
            print("Queue Empty")
        else:
            while temp_Node.next is not None:
                if temp_Node.data == data:      # 찾고자 하는 data와 일치할 때, data를 -1로 할당
                    temp_Node.data = -1
                    break
                else:
                    temp_Node = temp_Node.next  # 다음 노드를 가리키도록 설정
            return