class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def insert(self, root, data) -> Node:
        if root == None:
            root = Node(data)
            return root
        elif data <= root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def inorder_traversel(self, root) -> None:
        if root == None:
            return
        self.inorder_traversel(root.left)
        print(root.data, end=" ")
        self.inorder_traversel(root.right)
        return
    
    def find_height(self, root) -> int:
        if root == None:
            return -1
        leftHeight = self.find_height(root.left)
        rightHeight = self.find_height(root.right)
        return max(leftHeight, rightHeight) + 1
    
    def is_balanced(self, root) -> bool:
        if root is None:
            return True
        
        # Check if left subtree is balanced
        leftHeight = self.find_height(root.left)
        
        # Check if right subtree is balanced
        rightHeight = self.find_height(root.right)
        
        # Check if current node is balanced
        if abs(leftHeight - rightHeight) > 1:
            return False
        return True
        
if __name__ == "__main__":
    tree = BST()
    root = None
    
    root = tree.insert(root, 33)
    root = tree.insert(root, 20)
    root = tree.insert(root, 18)
    root = tree.insert(root, 15)
    root = tree.insert(root, 10)
    # root = tree.insert(root, 35)
    # root = tree.insert(root, 45)
    # root = tree.insert(root, 50)
    # root = tree.insert(root, 15)
    # root = tree.insert(root, 27)
    # root = tree.insert(root, 10)
    # root = tree.insert(root, 7)
    # root = tree.insert(root, 5)
    
    tree.inorder_traversel(root)
    print('\n')
    
    print('Height of tree: ', tree.find_height(root))
    
    print('Is balanced: ', tree.is_balanced(root))