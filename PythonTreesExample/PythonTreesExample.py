# Python Trees Example
# Written by M.Margalis for CS-4, Spring 2025

# Imported for use in the levelorder() function
from queue import Queue

# Class to be used for the binary tree nodes
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(root, newValue):
    #if binary search tree is empty, create a new node and declare it as root
    if root == None:
        root = BinaryTreeNode(newValue)
        return root
    # if newValue is less than value of data in root, add it to L subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than the value of data in root, add it to the R subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root

# Function for preorder traversal of the tree
def preorder(root):
    # if root is None, then return
    if root == None:
        return
    # print the current node
    print(root.data, end=" ,")
    # travarse right subtree
    preorder(root.rightChild)

# Function for postorder traversal of the tree
def postorder(root):
    # if root is None, then return
    if root == None:
        return
    # traverse left subtree
    postorder(root.leftChild)
    #traverse right subtree
    postorder(root.rightChild)
    #print the current node
    print(root.data, end=" ,")

# Function for levelorder traversal of the tree
def levelorder(root):
    Q = Queue()
    Q.put(root)
    while (not Q.empty()):
        node = Q.get()
        if node == None:
            continue
        print(node.data)
        Q.put(node.leftChild)
        Q.put(node.rightChild)

# Function for inorder traversal of the tree
def inorder(root):
    # if root is None, then return
    if root == None:
        return
    # traverse left subtree
    inorder(root.leftChild)
    # print the current node
    print(root.data, end=" ,")
    # traverse the right subtree
    inorder(root.rightChild)

##### Begin pre-cooked data for tests #####
node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(45)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(15)
node6 = BinaryTreeNode(30)
node7 = BinaryTreeNode(78)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7

root = node1
##### End Data #####


def main():
    print("~~~Python Tree Test Cases~~~")
    print("\n")

    print("Pre-order traversal of the binary tree is:")
    preorder(node1)
    print("\n", "\n")

    print("Post order traversal of the binary tree is:")
    postorder(root)
    print("\n", "\n")

    print("Level order traversal of the binary tree is:")
    levelorder(root)
    print("\n", "\n")

    print("In-order traversal of the binary tree is:")
    inorder(root)
    print("\n", "\n")
    return

main()