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
        new_node.next = self.head
        self.head = new_node
        return

    def search_recursive(self,list_pointer,key):
        if list_pointer == None:
            return False
        if list_pointer.data == key:
            return True
        return self.search_recursive(list_pointer.next,key)
    
    def print(self):
        if self.head == None:
            print("Empty")
            return
        itr = self.head
        while itr:
            print(f"{itr.data} --> ", end="")
            itr = itr.next
        print("\n")
        return


if __name__ == '__main__':
    llist = LinkedList()
    llist.push("Sabbir")
    llist.push("Hossain")
    llist.push("Bappy")
    search = "Hossain"
    item = llist.search_recursive(llist.head, search)
    print(item)
    if(item == True):
        print("Found")
    else:
        print("Not found")
    llist.print()
