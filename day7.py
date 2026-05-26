# class Node:

#     def __init__(self, data, left = None, right = None){
#         self.data = data 
#         self.left = left
#         self.right = right
#     }

# root = Node(5)
# root.left = Node(10)
# root.right = Node(20)
# root.left.left = Node(15)
# root.left.right = Node(30)
# root.right.left = Node(30)
# root.right.right = Node(25)

# from collections import deque
# class Node:

#     def __init__(self, data, left = None, right = None):
#         self.data = data

# class BT:
#     def insert(self, root, data):
#         newNode = Node(data)

#         if root is None:
#             return newNode

#         dq = deque([root])

#         while dq:
#             root = dq.popleft()

#             if root.left is None:
#                 root.left = newNode
#                 return

#             else:
#                 dq.append(root.left)

#             if root.right is None:
#                 root.right = newNode
#                 return
            
#             else:
#                 dq.append(root.right)

# bt = BT()

#----------------------------------------------------------
from collections import deque

class Node:

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BST:

    def __init__(self):
        self.root = None

    def insert(self, root, data):
        newNode = Node(data)

        if root is None:
            return newNode

        if data < root.data:
            root.left = self.insert(root.left, data)

        else:
            root.right = self.insert(root.right, data)

        return root
    
    def preOrder(self, root):

        if root is None:
            return
        
        print(root.data, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root):

        if root is None:
            return
        
        self.preOrder(root.left)
        self.preOrder(root.right)
        print(root.data, end = " ")

    def InOrder(self, root):

        if root is None:
            return
        
        self.preOrder(root.left)
        print(root.data, end = " ")
        self.preOrder(root.right)

    def height(self, root):

        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))
    
    def sumOfAllNodes(self, root):

        if root is None:
            return 0
        
        l_sum = self.sumOfAllNodes(root.left)
        r_sum = self.sumOfAllNodes(root.right)
        
        return r_sum + l_sum + root.data
        
    def countnumberOfNodes(self, root):

        if root is None:
            return 0
        
        l_count = self.countnumberOfNodes(root.left)
        r_count = self.countnumberOfNodes(root.right)

        return l_count + r_count + 1
    
    def binarysearch(self, root, key):              # Mine
        if root is None:
            return "No"
        
        if root.data == key:
            return "Yes"
        
        if key < root.data:
            return self.binarysearch(root.left, key)
        
        else:
            return self.binarysearch(root.right, key)
        
    def smallestValue(self, root):
        if root is None:
            return None

        if root.left is None:
            return root.data

        return self.smallestValue(root.left)
    
    # def smallestValue(self, root):    #GPT
    #     if root is None:
    #         return None

    #     while root.left:
    #         root = root.left

    #     return root.data
    
    def largestValue(self, root):
        if root is None:
            return None
        
        if root.right is None:
            return root.data
        
        return self.largestValue(root.right)

bst = BST()
root = None
root = bst.insert(root, 10)
root = bst.insert(root, 20)
root = bst.insert(root, 30)
root = bst.insert(root,  8)
root = bst.insert(root,  5)
root = bst.insert(root,  2)
root = bst.insert(root, 9)

#         10
#        /  \
#       8    20
#      / \     \
#     5   9     30
#    /
#   2

print("Root: ", root.data)      # Root:  10

print("Inorder: ")              #Inorder: 
bst.InOrder(root)               # 8 5 2 9 10 20 30  

print("\nPreorder: ")           # Preorder: 
bst.preOrder(root)              # 10 8 5 2 9 20 30 

print("\nPostorder: ")          # Postorder: 
bst.postOrder(root)             # 8 5 2 9 20 30 10

print("\nHeight of Tree: ", bst.height(root))       # Height of Tree:  4

print("Sum of all nodes: ", bst.sumOfAllNodes(root))    # Sum of all nodes:  84

print("Count of nodes: ", bst.countnumberOfNodes(root))     # Count of nodes:  7

print("Is 10 there?: ", bst.binarysearch(root, 10))    # Is 10 there?:  Yes

print("Smallest Value in Tree: ", bst.smallestValue(root))    # Smallest Value in Tree:  2
print("Largest Value in Tree: ", bst.largestValue(root))      # Largest Value in Tree:  30