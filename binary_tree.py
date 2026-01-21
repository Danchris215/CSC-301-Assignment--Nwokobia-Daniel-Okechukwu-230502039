class Node:
    def __init__(self, key):
        self.left = None 
        self.right = None 
        self.val = key 

#Left Root Right 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

#Root Left Right 
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

#Left Right Root 
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

def tree_height(root):
    if root is None:
        return 0 

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    #return the maximum of the two heights + 1 for the current node
    return max(left_height, right_height) + 1

#testing with a binary tree 
root = Node(23)
root.left = Node(5)
root.right = Node(18)
root.left.left = Node(70)
root.left.right = Node(10)
root.left.right.left = Node(8)

root.right.left = Node(15)
root.right.left.right = Node(12)


print("Inorder traversal:")
inorder(root)
print("\nPreorder traversal:")
preorder(root)
print("\nPostorder traversal:")
postorder(root)

print("\nTree height is: ", tree_height(root))
