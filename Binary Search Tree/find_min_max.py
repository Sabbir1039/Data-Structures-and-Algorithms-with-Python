from collections import deque

class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
def insert(data, root):
    if(root == None):
        new_node = BSTNode(data)
        root = new_node
        return root
    elif(data <= root.data):
        root.left = insert(data, root.left)
    else:
        root.right = insert(data, root.right)
    return root

def levelOrderTravarsal(root):
    if root == None:
        return
    d = deque()
    d.append(root)
    while(len(d) != 0):
        current = d.popleft()
        print(current.data, end="->")
        if (current.left != None):
            d.append(current.left)
        if (current.left != None):
            d.append(current.right)

# recursive function for finding min value
def findMin(root):
    if (root == None):
        return
    elif(root.left == None):
        return root.data
    else:
        return findMin(root.left)
    
# iterative function for finding min value
def findMinIterative(root):
    if (root == None):
        return 
    while(root.left != None):
        root = root.left
    return root.data

# recursive function for finding max value
def findMaxRecursive(root):
    if (root == None):
        return
    elif(root.right == None):
        return root.data
    else:
        return findMaxRecursive(root.right)
    
# Iterative function for finding min value
def findMaxIterative(root):
    if (root == None):
        return
    while(root.right != None):
        root = root.right
    return root.data
  
if __name__ == "__main__":
    root = None
    root = insert(20, root)
    root = insert(25, root)
    root = insert(15, root)
    root = insert(9, root)
    root = insert(18, root)
    root = insert(22, root)
    root = insert(28, root)
    levelOrderTravarsal(root)
    print()
    # min = findMin(root)
    # print(f"Min value in the tree = {min}")
    min = findMinIterative(root)
    print(f"Min value in the tree = {min}")
    
    # max = findMaxRecursive(root)
    # print(f"max = {max}")
    
    max = findMaxIterative(root)
    print(f"max = {max}")