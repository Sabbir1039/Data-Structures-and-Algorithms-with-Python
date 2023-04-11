# Stack implementation and operations using liked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            return
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = node
        return

    def pop(self):
        temp = self.head
        prev = None

        if(temp == None):
            print("Stack empty")

        while(temp.next != None):
            prev = temp
            temp = temp.next
        prev.next = None
        res = temp.data
        del temp
        return res
    
    def isEmpty(self):
        temp = self.head
        if(temp == None):
            return True
        else: 
            return False
    
    def peek(self):
        temp = self.head

        while(temp.next != None):
            temp = temp.next
        return temp.data
    
if __name__ == "__main__":
    
    S = Stack()

    print(f"Is stack is empty? {S.isEmpty()}")
    S.push("one")
    S.push("two")
    S.push("three")
    S.push("four")
    S.push("five")

    print(f"Top item = {S.peek()}")

    print(f"Popped item = {S.pop()}")

    print(f"Top item = {S.peek()}")
    
    print(f"Is stack is empty? {S.isEmpty()}")

    print(f"Popped item = {S.pop()}")

    print(f"Top item = {S.peek()}")

    