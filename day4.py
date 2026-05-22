# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# def show(n):
#     if(n==0):
#         return
#     print("Before Inside the function", n)
#     show(n-1)
#     print("After Inside the function", n)

# n = 3
# print("Before outside the function", n)
# show(n)
# print("After outside the function", n)

# def show(n):      # 1 - n
#     if(n == 0):
#         return
#     show(n - 1)
#     print(n)
    
# n = int(input("Enter N:"))
# show(n)

# def show(n):      # n - 1
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)
    
# n = int(input("Enter N:"))
# show(n)

# def show(i, n):      # 1 - n
#     if(i == n):
#         return
#     print(i)
#     show(i + 1, n)
    
# n = int(input("Enter N:"))
# show(1, n + 1)

# def sum_r(n):
#     if(n == 0):
#         return 0
#     return n + sum_r(n-1)

# n = int(input("Enter N:"))
# print(sum_r(n))

# def fact(n):
#     if(n == 0):
#         return 1
#     return n * fact(n-1)

# n = int(input("Enter N:"))
# print(fact(n))

# r = int(input("ENter R:"))

# print("Permutation: ", fact(n) / fact(n-r))
# print("Comnination: ", fact(n) / fact(n) * fact(n-r))

# def fibo(n):
#     if (n == 1) or (n==0):
#         return n
#     return fibo(n-1) + fibo(n-2)

# n = int(input("ENter n: "))
# print("Fibinacci sum: ", fibo(n))

# for i in range(n):
#     print(fibo(i), end=" ")

# def n_paths(i, j, n, m):
#     if i == n or j == m:
#         return 0
#     if i == n-1 and j == m-1:
#         return 1
#     right = n_paths(i, j+1, n, m)
#     down = n_paths(i+1, j, n, m)
#     return right + down

# m = int(input("Enter rows: "))
# n = int(input("Enter column: "))

# print("Total paths:", n_paths(0, 0, n, m))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return  
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  
        last_node.next = new_node
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
            

linked_list = LinkedList()
linked_list.insert(10)
linked_list.display()





