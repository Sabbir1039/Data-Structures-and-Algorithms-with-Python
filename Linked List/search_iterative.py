class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self,new_data):
        new_node = Node(new_data)

        if(self.head == None):
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        return
    
    def print(self):
        if(self.head == None):
            print("Empty")
        itr = self.head
        while itr:
            print(f"{itr.data} --> ",end="")
            itr = itr.next
        print("\n")
        return
    
    def search(self,x):
        temp = self.head
        while temp:
            if(temp.data == x):
                print("Found")
                return
            temp = temp.next
        print("Not Found")
    
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)
    llist.append(50)
    llist.print()
    llist.search(70)
    llist.search(20)