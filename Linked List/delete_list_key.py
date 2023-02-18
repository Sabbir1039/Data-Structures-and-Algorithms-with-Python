# Delete data from linked list by given value/key
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
    

    #delete nth node from given value/key
    def delete_key(self,key):
        temp = self.head
        prev = self.head
        if temp != None:
            if temp.data == key:
                self.head = temp.next
                temp = None
        while temp != None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None
        
           

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
    llist.delete_key(11)
    llist.print_node()