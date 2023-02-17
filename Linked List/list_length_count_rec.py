class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        return
    
    def print_rec(self,point):
        if point == None:
            return
        print(f"{point.data} --> ",end="")
        self.print_rec(point.next)

    # length count recursively with extra space

    # def length_count_rec(self,temp_head):
    #     if temp_head == None:
    #         return 0
    #     return 1 + self.length_count_rec(temp_head.next)
    
     # length count recursively without extra space
    def length_count_rec(self,temp_head, count = 0):
        if temp_head == None:
            return count
        return self.length_count_rec(temp_head.next, count + 1)
        
    
    def get_count(self):
        res = self.length_count_rec(self.head)
        print(f"Length of linked list = {res}")

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(5)
    llist.push(7)
    llist.push(9)
    llist.push(11)
    llist.push(13)
    llist.push(15)
    llist.push(17)
    llist.print_rec(llist.head)
    print("\n")
    llist.get_count()