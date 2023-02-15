class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_end(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        itr = self.head
        while itr.next != None:
            itr = itr.next
        itr.next = new_node

        return

    def print_node(self):
        itr = self.head
        if itr == None:
            print("Empty")
        while itr:
            print(f"{itr.data} -->", end=" ")
            itr = itr.next
        print("\n")
        return

if __name__ == '__main__':
    llist = LinkedList()
    llist.print_node()
    llist.insert_at_end(9)
    llist.print_node()
    llist.insert_at_end(7)
    llist.print_node()
    llist.insert_at_end(5)
    llist.print_node()
    llist.insert_at_end(3)
    llist.print_node()
    llist.insert_at_end(1)
    llist.print_node()