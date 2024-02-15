class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def push_left(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return
    
    def push_right(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        if temp == None:
            self.head = new_node
            return
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node
        return
    
    def push_at_nth(self, new_data, pos):
        new_node = Node(new_data)
        temp = self.head
        prev = None
        
        if pos == 0 or not temp:
            new_node.next = temp
            self.head = new_node
            return
        
        for _ in range(0, pos):
            prev = temp
            temp = temp.next
        prev.next = new_node
        new_node.next = temp
        return
    
    def delete_from_left(self):
        if self.head == None:
            print("List is empty")
            return False
        temp = self.head
        self.head = temp.next
        del temp
        return True
    
    def delete_from_right(self):
        if self.head == None:
            print("List is empty")
            return False
        temp = self.head
        prev = None
        while temp.next != None:
            prev = temp
            temp = temp.next
        prev.next = None
        del temp
        return True
    
    def delete_from_nth(self, pos):
        temp = self.head
        if temp == None:
            print('List is empty!')
            return False
        if pos == 0:
            self.head = temp.next
            del temp
            return True
        prev = None
        for _ in range(pos):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        del temp
        return True
    
    def search_extra_space(self, value):
        if self.head == None:
            print("List is empty")
            return False
        res = []
        temp = self.head
        while temp:
            res.append(temp.data)
            temp = temp.next
        if value in res:
            return True
        else:
            return False
        
    def search_iterative(self, value):
        if self.head == None:
            print("List is empty")
            return False
        temp = self.head
        while temp is not None:
            if temp.data == value:
                return True
            temp = temp.next
        return False
    
    def search_recursive(self, value, temp):
        if temp == None:
            return False
        if temp.data == value:
            return True
        return self.search_recursive(value, temp.next)
    
    def print_node(self):
        temp = self.head
        while(temp):
            print(f'{temp.data} -> ', end=' ')
            temp = temp.next
        print('\n')
        return
    
    def print_node_recursively(self, temp):
        if temp is None:
            return
        print(f'{temp.data} -> ', end=" ")
        self.print_node_recursively(temp.next)
        return
    
    def reverse_list_iterative(self):
        temp = None
        prev = None
        curr = self.head
        if curr is None:
            print("List is empty")
            return
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        return
            
    def reverse_list_recursive(self, temp):
        if temp is None or temp.next is None:
            return temp
        result = self.reverse_list_recursive(temp.next)
        temp.next.next = temp
        temp.next = None
        return result
        

if __name__ == "__main__":
    llist = LinkedList()
    llist.push_right(1)
    llist.push_right(2)
    llist.push_right(3)
    llist.print_node()
    head = llist.reverse_list_recursive(llist.head)
    llist.print_node_recursively(head)