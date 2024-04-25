# This is another approach to check is the tree is BST or not, works in every scenario
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    
    # method for insertion bst tre node using recursion
    def insert(self, root, data):
        if(root == None):
            new_node = Node(data)
            root = new_node
            return root
        elif(data < root.data):
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    # wrong binary search tree
    def insertWrongTree(self, root, data):
        if root == None:
            new_node = Node(data)
            root = new_node
            return root
        elif(data > root.data):
            root.left = self.insertWrongTree(root.left, data)
        else:
            root.right = self.insertWrongTree(root.right, data)
        return root
            
    def inorderTraversal(self, head):
        if head is None:
            return
        self.inorderTraversal(head.left)
        print(head.data, end=" ")
        self.inorderTraversal(head.right)
        return
    
    def isBST(self, root):
        if root is None:
            return True
        nodes = []
        
        def inorder(head):
            if head is None:
                return
            inorder(head.left)
            nodes.append(head.data)
            inorder(head.right)
            return
        
        inorder(root)
        
        # now checking if nodes = [] list sorted or not
        prev = nodes[0]
        
        for i in range(1, len(nodes)-1):
            if nodes[i] <= prev:
                return False
            prev = nodes[i]
        
        return True
        
        
            

if __name__ == "__main__":
    
    tree  = BST()
    root = None
    
    root = tree.insert(root, 20)
    root = tree.insert(root, 15)
    root = tree.insert(root, 25)
    root = tree.insert(root, 9)
    root = tree.insert(root, 18)
    root = tree.insert(root, 22)
    root = tree.insert(root, 28)
    
    wrongTree = BST()
    head = None
    
    head = wrongTree.insertWrongTree(head, 15)
    head = wrongTree.insertWrongTree(head, 20)
    head = wrongTree.insertWrongTree(head, 16)
    
    wrongTree.inorderTraversal(head)
    print(wrongTree.isBST(head))
  
    