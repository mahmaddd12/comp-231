
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


def insert_BTnode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left_child is None:
                root.left_child = node
            else:
                insert_BTnode(root.left_child, node)
        else:
            if root.right_child is None:
                root.right_child = node
            else:
                insert_BTnode(root.right_child, node)

# 1 This function will create BST and return root node of 
# tree using the node data from the file 
def make_BST(file_name):
    
    list_data = [] ## intitializing list of the nodes
    with open(file_name, 'r') as f:
        # read all value and append to list data 
        for i in f:
            list_data.append(int(i))

    # create root node 
    root_node = Node(list_data[0])
    n = len(list_data)
    # add ramaining node one by one 
    for i in range(1, n):
        insert_BTnode(root_node, Node(list_data[i]))

    # return root_node
    return root_node


if __name__ == '__main__':
    my_root = make_BST("PS5_sample.txt") ##call the make_BST function