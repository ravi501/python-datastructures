
from trees.Node import Node


def print_inorder(root):
    if root:
        print_inorder(root.left)

        print(root.data)

        print_inorder(root.right)


def print_pre_order(root):
    if root:
        print(root.data)

        print_pre_order(root.left)

        print_pre_order(root.right)


def print_post_order(root):
    if root:

        print_post_order(root.left)

        print_post_order(root.right)

        print(root.data)


root = Node(1)
root.data = 1
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal of binary tree is")
print_pre_order(root)

print("\nInorder traversal of binary tree is")
print_inorder(root)

print("\nPostorder traversal of binary tree is")
print_post_order(root)
