class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self) -> None:
        self.root = None
    
    # method for insertion bst tre node using recursion
    def insertionRecursive(self, root, data):
        if(root == None):
            new_node = BSTNode(data)
            root = new_node
            return root
        elif(data <= root.data):
            root.left = self.insertionRecursive(root.left, data)
        else:
            root.right = self.insertionRecursive(root.right, data)
        return root
            
    
    # method for insertion bst tre node non-recursive way
    def insert(self, data):
        newNode = BSTNode(data)
        head = self.head
        
        if head is None:
            self.head = newNode
            return
        curr = head
        
        while True:
            if data <= curr.data:
                if curr.left is None:
                    curr.left = newNode
                    return
                curr = curr.left
            
            else:
                if curr.right is None:
                    curr.right = newNode
                    return
                curr = curr.right