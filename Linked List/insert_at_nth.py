class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_first(self,new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node
        return

    def insert_at_nth(self,pos,new_data):
        temp = self.head
        new_node = Node(new_data)
        if (temp == None) or (pos == 0):
            print("Invalid Position")
            return
        for _ in range(pos-2):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        return


    def print(self):
        itr = self.head
        if itr == None:
            print('Empty')
            return
        while itr:
            print(f"{itr.data} -->",end=" ")
            itr = itr.next
        print("\n")
        return

if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_nth(1,50)
    llist.insert_at_first(30)
    llist.insert_at_first(20)
    llist.insert_at_first(10)
    llist.print()
    llist.insert_at_nth(2,50)
    llist.print()