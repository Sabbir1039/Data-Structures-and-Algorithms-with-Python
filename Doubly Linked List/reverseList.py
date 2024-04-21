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
    
    # method for reverse doubly linked list non-recursive
    def reverseDoublyLinkedList(self):
        head = self.head
        if head is None:
            return
        self.tail = head
        temp = None
        
        while head:
            nxt = head.next
            head.prev = head.next
            head.next = temp
            temp = head
            head = nxt
        self.head = temp
        
    def reverseDoublyLinkedListRecursive(self, head):
        temp = head
        if temp is None or temp.next is None:
            return temp
        
        retNode = self.reverseDoublyLinkedListRecursive(temp.next)
        temp.prev = temp.next
        temp.next.next = temp
        temp.next = None
        
        return retNode
        
if __name__ == '__main__':
    llist = DoublyLinkedList()
    llist.insert(10)
    llist.insert(9)
    llist.insert(8)
    llist.insert(7)
    llist.insert(6)
    llist.insert(5)
    
    head = llist.reverseDoublyLinkedListRecursive(llist.head)
    llist.head = head
    llist.printList()
    