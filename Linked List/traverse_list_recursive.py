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
    
#  function for travarse a linked list
    def print_rec(self,itr):
        if itr == None:
            return
        print(f"{itr.data} --> ", end="")
        self.print_rec(itr.next)


if __name__ == '__main__':
    llist = LinkedList()
    llist.push("Sabbir")
    llist.push("Hossain")
    llist.push("Bappy")
    llist.print_rec(llist.head)
