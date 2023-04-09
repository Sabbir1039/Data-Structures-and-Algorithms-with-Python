# Stack implementation and stack operations with array/list

class Stack:

    def __init__(self):
        self.stack_list = []
        self.top = -1
    
    def push(self, data):
        self.top = self.top + 1
        self.stack_list.append(data)
        return
    
    def pop(self):
        if(self.isEmpty()):
            return None
        else:
            self.top = self.top - 1
            return self.stack_list.pop()
    
    def peek(self):
        return self.stack_list[self.top]
    
    def isEmpty(self):
        return (len(self.stack_list) == 0)
    
    def stack_size(self):
        return len(self.stack_list)

if __name__ == '__main__':

    s = Stack()
    print("Is list empty? ",s.isEmpty())
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    print("Peek = ",s.peek())
    print("Popped item = ",s.pop())
    print("Peek = ",s.peek())
    print(f"Stack size = ", s.stack_size())

    s2 = Stack()
    print(s2.isEmpty())
    s2.push("Sabbir")
    s2.push("Rohan")
    s2.push("Moshaheb")
    s2.push("Promita")
    print(s2.stack_size())
    print(s2.peek())
    