class Node:
    def __init__(self,  data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
    
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insert(self, data):
        newNode = Node(data)
        head = self.head
        
        if head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = head
        head.prev = newNode
        self.head = newNode
        return
    
    def printList(self):
        head = self.head
        if head is None:
            return
        while head:
            print(f"{head.data} -> ", end='')
            head = head.next
    
    def printReverse(self):
        tail = self.tail
        if tail is None:
            return
        while tail:
            print(f"{tail.data} -> ", end='')
            tail = tail.prev

if __name__ == '__main__':
    llist = DoublyLinkedList()
    llist.insert(10)
    llist.insert(9)
    llist.insert(8)
    llist.insert(7)
    llist.insert(6)
    llist.insert(5)
    
    print(llist.head.data)
    print(llist.tail.data)
    print(llist.printList())
    print(llist.printReverse())
    