import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
class BST:   
    def insert(self, data, head):
        if head is None:
            newNode = Node(data)
            return newNode
        elif data <= head.data:
            head.left = self.insert(data, head.left)
        else:
            head.right = self.insert(data, head.right)
        return head
    
    # Create a graph from the tree
    def add_edges(self, G, node):
        if node.left:
            G.add_edge(node.data, node.left.data)
            self.add_edges(G, node.left)
        if node.right:
            G.add_edge(node.data, node.right.data)
            self.add_edges(G, node.right)


if __name__ == "__main__":
    # Raw data
    raw_data = "37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19 3"
    data_list = [int(x) for x in raw_data.split(" ")]

    tree = BST()
    root = None
    
    for data in data_list:
        root = tree.insert(data, root)

    G = nx.DiGraph()
    tree.add_edges(G, root)

    # Visualize the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=12)
    plt.show()
