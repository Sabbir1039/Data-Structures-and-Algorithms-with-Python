class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self) -> None:
        self.root = None
    
    def insertion(self, root, data):
        if(root == None):
            new_node = BSTNode(data)
            root = new_node
            return root
        elif(data <= root.data):
            root.left = self.insertion(root, data)
        else:
            root.right = self.insertion(root, data)