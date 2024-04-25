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
    
    def topView(self, head):
        if head is None:
            return
        dic = {}
        
        # level-order traversal using a queue
        que = [(head, 0)] # (node, horizontal distance)
         
        while que:
            node, hd = que.pop(0)
            
            # If the horizontal distance is not in the dictionary, add the node
            if hd not in dic:
                dic[hd] = node.data
                
            # Enqueue left child with hd-1 and right child with hd+1
            if node.left:
                que.append((node.left, hd-1))
            if node.right:
                que.append((node.right, hd+1))
        
        for hd in sorted(dic.keys()):
            print(dic[hd], end=" ")
        
        return
    
        
if __name__ == "__main__":
    tree = BST()
    root = None
    
    root = tree.insert(root, 15)
    root = tree.insert(root, 20)
    root = tree.insert(root, 10)
    root = tree.insert(root, 5)
    root = tree.insert(root, 17)
    root = tree.insert(root, 25)
    root = tree.insert(root, 16)
    root = tree.insert(root, 30)
    root = tree.insert(root, 50)
    
    tree.inorder_traversel(root)
    
    print()
    
    tree.topView(root)