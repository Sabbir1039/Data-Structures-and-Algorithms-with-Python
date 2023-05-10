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
    
# function for finding height of bst tree
def findHeight(root):
    if root == None:
        return -1
    leftHeight = findHeight(root.left)
    rightHeight = findHeight(root.right)
    return max(leftHeight, rightHeight)+1


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
    print(f"height of bst = {findHeight(root)}")
    