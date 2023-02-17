class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def push(self,new_data):
        node = Node(new_data)
        if self.head == None:
            self.head = node
            return
        itr = self.head
        while itr.next != None:
            itr = itr.next
        itr.next = node
        return
    
    def print(self):
        itr = self.head
        if itr ==None:
            print("Empty")
            return
        while itr:
            print(f"{itr.data} --> ",end="")
            itr = itr.next
        print("\n")
        return

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)
    llist.push(50)
    llist.print()

    # Search x = 30 
    x = 90
    linked_list = []

    temp = llist.head
    while temp.next != None:
        linked_list.append(temp.data)
        temp = temp.next
    
    for i in range(len(linked_list)):
        if(linked_list[i] == x):
            print("Found")
    print("Not Found")
