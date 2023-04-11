# Queue implementation and operations using liked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
    
    def enqueue(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            return
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = node
        return
    
    def dequeue(self):
        if(self.head == None):
            return "Empty"
        temp = self.head
        self.head = temp.next
        res = temp.data
        del temp
        return res
    
    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
    
    def peek(self):
        temp = self.head
        if(self.head == None):
            return "Empty"
        else:
            return temp.data
        
if __name__ == "__main__":

    Q = Queue()
    print(f"Is queue empty ? {Q.isEmpty()}")
    Q.enqueue("one")
    Q.enqueue("two")
    Q.enqueue("three")
    print(f"Is queue empty ? {Q.isEmpty()}")
    print(f"Top item = {Q.peek()}")
    print(f"Dequeue item = {Q.dequeue()}")
    print(f"Top item = {Q.peek()}")