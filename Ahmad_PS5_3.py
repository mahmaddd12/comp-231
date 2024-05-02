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
    # add remaining node one by one 
    for i in range(1, n):
        insert_BTnode(root_node, Node(list_data[i]))

    # return root_node
    return root_node



# 3 This function returns the list of visited order of DFS on the given tree 
def DFS_my_BST(node):
    # Initializing To store DFS visited nodes
    DFS_list = []
    
    # create nested DFS function (for recursive call)
    def DFS(node):
        # if node is not None then only call recursively 
        if(node != None):
            # first call child nodes 
            DFS(node.left_child)
            DFS(node.right_child)
            # append node data to DFS_list
            DFS_list.append(node.data)

    # call DFS function - this function fills the DFS_list
    DFS(node)

    # return DFS_list
    return DFS_list

if __name__ == '__main__':
    my_root = make_BST("PS5_sample.txt")
    print("DFS_my_BST :", DFS_my_BST(my_root))
    