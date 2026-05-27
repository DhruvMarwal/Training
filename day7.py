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
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end = " ")

    def InOrder(self, root):
        if root is None:
            return
        
        self.InOrder(root.left)
        print(root.data, end = " ")
        self.InOrder(root.right)

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
    
    def binarySearchCheck(self, root, key):              # Mine
        if root is None:
            return "No"
        
        if root.data == key:
            return "Yes"
        
        if key < root.data:
            return self.binarysearch(root.left, key)
        
        else:
            return self.binarysearch(root.right, key)
        
    def binarysearch(self, root, key):              # Mine
        if root is None:
            return "No"
        
        if root.data == key:
            return root
        
        if key < root.data:
            return self.binarysearch(root.left, key)
        
        else:
            return self.binarysearch(root.right, key)
        
    def smallestValue(self, root):      # returns adddress of smallest root
        if root is None:
            return None

        if root.left is None:
            return root

        return self.smallestValue(root.left)
    
    # def smallestValue(self, root):    #GPT
    #     if root is None:
    #         return None

    #     while root.left:
    #         root = root.left

    #     return root.data
    
    def largestValue(self, root):       # returns valus of largest root
        if root is None:
            return None
        
        if root.right is None:
            return root.data
        
        return self.largestValue(root.right)
    
    # def delete0child(self, root, key):        # Mine
    #     root = self.binarysearch(root, key)
    #     root.data = None

    # def delete1child(self, root, key):
    #     root = self.binarysearch(root, key)

    #     if root.left is None:
    #         root.right = None

    #     if root.right is None:        
    #         root.left = None

    # def deletemid(self, root, key):
    #     root = self.binarysearch(root,key)
    #     root.data = self.smallestValue(root.right)

    def deleteNode(self, root, key):

        if root is None:
            return None
        
        if key < root.data:
            root.left = self.deleteNode(root.left, key)

        elif key > root.data:
            root.right = self.deleteNode(root.right, key)

        else:
            # 0 child
            if root.left is None and root.right is None:
                return None
            
            # 1 child
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left
            
            # 2 child
            else:
                iso = self.smallestValue(root.right)
                root.data = iso.data
                self.deleteNode(root.right, iso.data)

        return root


bst = BST()
root = None
arr = [10, 20, 18, 30, 8, 5, 2, 9]
for i in arr:
    root = bst.insert(root, i)

# root = bst.insert(root, 10)
# root = bst.insert(root, 20)
# root = bst.insert(root, 18)
# root = bst.insert(root, 30)
# root = bst.insert(root,  8)
# root = bst.insert(root,  5)
# root = bst.insert(root,  2)
# root = bst.insert(root,  9)

#          10
#        /    \
#       8      20
#      / \    /  \
#     5   9 18    30
#    /
#   2

print("Root: ", root.data)      # Root:  10

print("Inorder: ")              #Inorder: 
bst.InOrder(root)               # 2 5 8 9 10 18 20 30
print()

print("\nPreorder: ")           # Preorder: 
bst.preOrder(root)              # 10 8 5 2 9 20 18 30
print()

print("\nPostorder: ")          # Postorder: 
bst.postOrder(root)             # 2 5 9 8 18 30 20 10 
print()

print("\nHeight of Tree: ", bst.height(root))       # Height of Tree:  4

print("Sum of all nodes: ", bst.sumOfAllNodes(root))    # Sum of all nodes: 102

print("Count of nodes: ", bst.countnumberOfNodes(root))     # Count of nodes:  8

print("Is 10 there?: ", bst.binarySearchCheck(root, 10))    # Is 10 there?:  Yes
print("Is 10 there?: ", bst.binarysearch(root, 10))    # Is 10 there?:  <__main__.Node object at 0x000001DEDC0B01A0>

print("Smallest Value in Tree: ", bst.smallestValue(root).data)    # Smallest Value in Tree:  2
print("Largest Value in Tree: ", bst.largestValue(root))      # Largest Value in Tree:  30


# # Orginal InOrder: 2 5 8 9 10 18 20 30  

# root = bst.deleteNode(root, 10)   # Delete 2 child
# print("\nInorder: ")              # Inorder: 
# bst.InOrder(root)                 # 2 5 8 9 18 20 30  

# root = bst.deleteNode(root, 18)   # Delete 0 Child
# print("\nInorder: ")              #Inorder: 
# bst.InOrder(root)                 # 2 5 8 9 10 20 30 

# root = bst.deleteNode(root, 5)    # Delete 1 child
# print("\nInorder: ")              #Inorder: 
# bst.InOrder(root)                 # 2 8 9 10 18 20 30 