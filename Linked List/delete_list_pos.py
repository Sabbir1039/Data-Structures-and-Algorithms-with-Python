# Delete data from linked list by given position
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    #insert node at the end of the list
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
    #print data of linked list
    def print_node(self):
        itr = self.head
        if itr == None:
            print("Empty")
        while itr:
            print(f"{itr.data} -->", end=" ")
            itr = itr.next
        print("\n")
        return
    
    #delete first node
    def delete_first(self):
        temp = self.head
        if (self.head != None):
            self.head = temp.next
            del temp
            return

    #delete last node
    def delete_last(self):
        temp = self.head
        prev = self.head
        if(temp != None):
            while temp.next != None:
                prev = temp
                temp = temp.next
            prev.next = None
            del temp
            return

    #delete nth node
    def delete_nth(self,pos):
        temp = self.head
        prev = self.head
        for i in range(0,pos):
            if i == 0 and pos == 1:
                self.head = temp.next
                del temp
                return
            else:
                if i == pos-1 and temp is not None:
                    prev.next = temp.next
                    del temp
                    return
                else:
                    prev = temp
                    if prev is None:
                        break
                    temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_end(3)
    llist.insert_at_end(5)
    llist.insert_at_end(7)
    llist.insert_at_end(9)
    llist.insert_at_end(11)
    llist.insert_at_end(13)
    llist.insert_at_end(15)
    llist.insert_at_end(17)
    llist.insert_at_end(19)
    llist.print_node()
    llist.delete_first()
    llist.print_node()
    llist.delete_last()
    llist.print_node()
    llist.delete_nth(8)
    llist.print_node()