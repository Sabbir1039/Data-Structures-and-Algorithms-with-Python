from collections import deque

class BSTNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BSTtree:
    def node_insertion(self, root, data):
        if(root == None):
            new_node = BSTNode(data)
            root = new_node
            return root
        elif(data <= root.data):
            root.left = self.node_insertion(root.left, data)
        else:
            root.right = self.node_insertion(root.right, data)
        return root
    
    # Level Order Tree Travarsal
    def levelOrderTravarsal(self, root):
        if(root == None):
            return
        d = deque()
        d.append(root)

        while(len(d) != 0):
            current = d.popleft()
            print(current.data, end=" -> ")

            if(current.left != None):
                d.append(current.left)
            if(current.right != None):
                d.append(current.right)

    # PreOrder Tree Travarsal
    def preOrder(self, root):
        if(root == None):
            return
        print(root.data, end=" -> ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    # In-Order Tree Travarsal
    def inOrder(self, root):
        if(root == None):
            return
        self.inOrder(root.left)
        print(root.data, end=" -> ")
        self.inOrder(root.right)

    # Post-Order Tree Travarsal
    def postOrder(self, root):
        if(root == None):
            return 
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" -> ")
    

if __name__ == "__main__":
    bst = BSTtree()
    root = None

    root = bst.node_insertion(root, 20)
    root = bst.node_insertion(root, 15)
    root = bst.node_insertion(root, 25)
    root = bst.node_insertion(root, 10)
    root = bst.node_insertion(root, 18)
    root = bst.node_insertion(root, 22)
    root = bst.node_insertion(root, 30)

    # print bst elements with level-order mananer BFS
    print('Level Order travarsal')
    bst.levelOrderTravarsal(root)

    print('\n')

    print('Pre Order travarsal')
    # print bst elements with pre-order mananer DFS
    bst.preOrder(root)

    print('\n')
    
    print('In Order travarsal')
    # print bst elements with in-order mananer DFS
    bst.inOrder(root)

    print('\nPost Order travarsal')
    # print bst elements with post-order mananer DFS
    bst.postOrder(root)

