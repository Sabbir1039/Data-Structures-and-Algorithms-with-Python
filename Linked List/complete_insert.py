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
    
    def insert_at_nth(self,pos,new_data):
        new_node = Node(new_data)

        if (pos == 0) or (self.head == None):
            print("Cant insert new node!")
        itr = self.head
        for _ in range(pos-2):
            itr = itr.next
        new_node.next = itr.next
        itr.next = new_node
        return

    def print(self):
        itr = self.head
        if itr == None:
            print("Empty")
        while itr:
            print(f"{itr.data} --> ",end="")
            itr = itr.next
        print("\n")
        return

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_first("Sabbir")
    llist.insert_at_first("Rohan")
    llist.print()
    llist.insert_at_end("Mahin")
    llist.insert_at_end("Sadman")
    llist.print()
    llist.insert_at_nth(2,"Moshaheb")
    llist.insert_at_nth(2,"Abir")
    llist.print()

