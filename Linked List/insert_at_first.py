class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_first(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        itr = self.head
        if itr == None:
            print("Empty")
            return
        while itr:
            print(f"{itr.data} -->",end=" ")
            itr = itr.next
        return
    
if __name__ == '__main__':

    llist = LinkedList()

    llist.insert_at_first(50)
    llist.insert_at_first(40)
    llist.insert_at_first(30)
    llist.insert_at_first(20)
    llist.insert_at_first(10)
    llist.insert_at_first(0)

    llist.print()