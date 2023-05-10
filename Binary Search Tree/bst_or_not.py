class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
def insert(data, root):
    if root == None:
        new_node = BSTNode(data)
        root = new_node
        return root
    elif(data <= root.data):
        root.left = insert(data, root.left)
    else:
        root.right = insert(data, root.right)
    return root

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end="->")
    inorder(root.right)
    return

# function for checking sub tree is lesser or not
def isSubTreeLesser(root, data):
    if root == None:
        return True
    elif(root.data <= data):
        return True
    else:
        return False

# function for checking sub tree is greater or not
def isSubTreeGreater(root, data):
    if root == None:
        return True
    elif(root.data > data):
        return True
    else:
        return False

# function for checking if a tree is binary or not
def isBinaryTree(root):
    if(root == None):
        return True
    elif(isSubTreeLesser(root.left, root.data) and (isSubTreeGreater(root.right, root.data)) and isBinaryTree(root.left) and isBinaryTree(root.right)):
        return True
    else:
        return False
    
# wrong binary tree
def insertWrongTree(data, root):
    if root == None:
        new_node = BSTNode(data)
        root = new_node
        return root
    elif(data > root.data):
        root.left = insertWrongTree(data, root.left)
    else:
        root.right = insertWrongTree(data, root.right)
    return root


if __name__ == "__main__":
    root = None
    root = insert(20, root)
    root = insert(15, root)
    root = insert(25, root)
    root = insert(9, root)
    root = insert(18, root)
    root = insert(22, root)
    root = insert(28, root)
    inorder(root)
    print()
    print(isBinaryTree(root))
    
    root2 = None
    root2 = insertWrongTree(20, root2)
    root2 = insertWrongTree(18, root2)
    root2 = insertWrongTree(15, root2)
    root2 = insertWrongTree(19, root2)
    root2 = insertWrongTree(22, root2)
    root2 = insertWrongTree(25, root2)
    root2 = insertWrongTree(21, root2)
    inorder(root2)
    print()
    print(isBinaryTree(root2))