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
    
    # function for reverse a linked list
    def reverse_list(self):
        curr = self.head
        prev = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
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
    llist.push("Ragib")
    llist.push("Rohan")
    llist.print_rec(llist.head)
    print("\n")
    llist.reverse_list()
    llist.print_rec(llist.head)
