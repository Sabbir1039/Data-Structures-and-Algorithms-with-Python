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

def findMin(root):
    if (root == None):
        return root
    elif(root.left == None):
        return root
    else:
        return findMin(root.left)  

def delete(key, root):
    if root == None:
        return root
    elif(key < root.data):
        root.left = delete(key, root.left)
    elif(key > root.data):
        root.right = delete(key, root.right)
    else:
        if (root.left == None) and (root.right == None):
            del root
            root = None
    
        elif(root.left == None):
            temp = root
            root = temp.right
            del temp
            
        elif(root.right == None):
            temp = root
            root = root.left
            del temp
            
        else:
            temp = findMin(root.right)
            root.data = temp.data
            root.right = delete(temp.data, root.right)
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
    delete(25, root)
    inorder(root)
    
   