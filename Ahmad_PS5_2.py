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

# 2 This function return list of visited order of BFS on given tree  
def BFS_my_BST(node):
    # To store BFS visited node 
    BFS_list = []
    # queue 
    q = []
    # first node 
    q.append(node)
    # run until queue become empty.
    while len(q) != 0:
        # save first node 
        node_copy = q[0]
        # remove first element from queue (pop the queue)
        q.pop(0)
        # append data from saved node to BFS_list
        BFS_list.append(node_copy.data)
        # if child node is not None then append node to queue (push)
        if(node_copy.left_child != None):
            q.append(node_copy.left_child)
        if(node_copy.right_child != None):
            q.append(node_copy.right_child)

    # return BFS_list
    return BFS_list




if __name__ == '__main__':
    my_root = make_BST("PS5_sample.txt")
    print("BFS_my_BST :", BFS_my_BST(my_root)) ##calling BFS_my_BST function

