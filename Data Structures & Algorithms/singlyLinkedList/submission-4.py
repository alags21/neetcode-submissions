class LinkedList:

    class Node:
        def __init__(self, val: int, next: "Node"):
            self.val = val
            self.next = next


    def __init__(self):
        self.head = None
        self.tail = None
        self.size: int = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for i in range(index):
            curr = curr.next
        
        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        node = LinkedList.Node(val, self.head)

        self.head = node

        if self.tail is None:
            self.tail = node

        self.size += 1

    def insertTail(self, val: int) -> None:
        node = LinkedList.Node(val, None)

        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return True

        curr = self.head
        for i in range(index - 1):
            curr = curr.next
        
        if curr.next == self.tail:
            self.tail = curr
        
        curr.next = curr.next.next
        self.size -= 1
        return True


    def getValues(self) -> List[int]:
        vals: List[int] = []
        curr = self.head
        for i in range(self.size):
            if curr == None:
                return vals
            vals.append(curr.val)
            curr = curr.next
        return vals