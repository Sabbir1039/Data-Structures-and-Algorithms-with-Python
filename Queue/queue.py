# Queue implementation and operations with array/list
class Queue:

    def __init__(self):
        self.queue_list = []
    
    def enqueue(self, data):
        self.queue_list.append(data)
    
    def dequeue(self):
        if(self.isEmpty()):
            return None
        else:
            return self.queue_list.pop(0)
    
    def isEmpty(self):
        return (len(self.queue_list) == 0)
    
    def peek(self):
        return self.queue_list[0]
    
    def size(self):
        return len(self.queue_list)
    

if __name__ == "__main__":

    q = Queue()

    q.enqueue("one")
    q.enqueue("two")
    q.enqueue("three")
    q.enqueue("four")

    print("Peek = ",q.peek())
    q.dequeue()
    print("Queue Size = ", q.size())