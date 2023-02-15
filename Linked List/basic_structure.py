class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print(self):
        itr = self.head
        if itr == None:
            print("Empty")
            return
        llist = ""
        while itr:
            llist += (str(itr.data) + "-->")
            itr = itr.next
        print(llist)

if __name__ =="__main__":
    llist = LinkedList()
    llist.print()
