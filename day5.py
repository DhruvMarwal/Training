# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LL:
#     def __init__(self):
#         self.head = None

#     def printList(self):
#         currentNode = self.head
#         while currentNode != None:
#             print(currentNode.data, end = " -> ")
#             currentNode = currentNode.next
#         print(None)

# newNode = Node(4)
# secondNode = Node(10)
# thirdNode = Node(20)

# newNode.next = secondNode
# secondNode.next = thirdNode

# List1 = LL()
# List1.head = newNode
# List1.printList()

# LL ------------------------------------------------------

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LL:
#     def __init__(self):
#         self.head = None

#     def prepend(self,data):
#         newNode = Node(data)

#         if self.head is not None:
#             newNode.next = self.head
            
#         self.head = newNode

#     # def prepend(self,data):           # broken
#     #         newNode = Node(data)

#     #         if self.head is not None:
#     #             newNode.next = self.head

#     #         else: 
#     #             self.head = newNode


#     def append(self, data):
#         newNode = Node(data)

#         if self.head is None:
#             self.head = newNode

#         else:
#             currentNode = self.head

#             while currentNode.next != None:     # while currentNode.next:
#                 currentNode = currentNode.next

#             currentNode.next = newNode

#     def delete_end(self):
#         currentNode = self.head

#         while currentNode.next.next != None:
#             currentNode = currentNode.next

#         currentNode.next = None
    
#     def delete_bet(self, data):
#         if self.head.data == data:
#             self.head = self.head.next

#         currentNode = self.head

#         while currentNode.next != None and currentNode.next.data != data:
#             currentNode = currentNode.next

#         if currentNode.next is not None:
#             currentNode.next = currentNode.next.next

#     def delete_start(self):
#         self.head = self.head.next

#     def printList(self):
#         currentNode = self.head

#         while currentNode != None:
#             print(currentNode.data, end = " -> ")
#             currentNode = currentNode.next

#         print(None)

# print("LL: ")
# L2 = LL()

# L2.prepend(4)
# L2.prepend(3)
# L2.prepend(2)
# L2.prepend(1)
# L2.prepend(0)
# L2.append(5)
# L2.append(6)
# L2.append(7)
# L2.append(8)
# L2.printList()              # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None

# L2.delete_end()
# L2.printList()              # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None

# L2.delete_start()
# L2.printList()              # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None

# L2.delete_bet(4)            # 1 -> 2 -> 3 -> 5 -> 6 -> 7 -> None
# L2.printList()

# Doubly LL ------------------------------------------------------

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DLL:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def prepend(self,data):
#         newNode = Node(data)

#         if self.head is not None:
#             newNode.next = self.head
#             self.head.prev = newNode
#             self.head = newNode
#         else:
#             self.head = newNode
#             self.tail = newNode

#     def append(self, data):
#         newNode = Node(data)

#         if self.head is None:
#             self.head = newNode
#             self.tail = newNode

#         else:
#             self.tail.next = newNode
#             newNode.prev = self.tail
#             self.tail = newNode


#     def delete_end(self):
#         if self.head is None:
#             self.print("LL is Empty!!!")

#         if self.head == self.tail:
#             self.head = None
#             self.tail = None

#         self.tail = self.tail.prev
#         self.tail.next = None

#     def delete_start(self):
#         if self.head is None:
#             self.print("LL is Empty!!!")
#         if self.head == self.tail:
#             self.head = None
#             self.tail = None
#             return

#         self.head = self.head.next
#         self.head.prev = None

#     def printList(self):
#         currentNode = self.head

#         while currentNode != None:
#             print(currentNode.data, end = " <--> ")
#             currentNode = currentNode.next

#         print(None)

#     def print_reverse_List(self):
#         currentNode = self.tail

#         while currentNode != None:
#             print(currentNode.data, end = " <--> ")
#             currentNode = currentNode.prev

#         print(None)

# print("DLL: ")
# L2 = DLL()

# L2.prepend(4)
# L2.prepend(3)
# L2.prepend(2)
# L2.prepend(1)
# L2.prepend(0)
# L2.append(5)
# L2.append(6)
# L2.append(7)
# L2.append(8)
# L2.printList()              # 0 <--> 1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6 <--> 7 <--> 8 <-->None
# L2.print_reverse_List()     # 8 <--> 7 <--> 6 <--> 5 <--> 4 <--> 3 <--> 2 <--> 1 <--> 0 <-->None

# L2.delete_end()
# L2.printList()              # 0 <--> 1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6 <--> 7 <-->None

# L2.delete_start()
# L2.printList()              # 1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6 <--> 7 <-->None


# Circle LL ------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self,data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode

        else:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode

        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = self.head
            self.head.prev = newNode
            self.tail = newNode


    def delete_end(self):
        if self.head is None:
            print("LL is Empty!!!")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
    
    def delete_start(self):
        if self.head is None:
            print("LL is Empty!!!")
            return

        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return

        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head

    def printList(self):
        if self.head is None:
            print(None)
            return

        currentNode = self.head

        while currentNode != self.tail:
            print(currentNode.data, end = " <--> ")
            currentNode = currentNode.next

        if self.head is not None:
            print(currentNode.data, end = " <-->")

        print(None)

    def print_reverse_List(self):
        if self.tail is None:
            print(None)
            return

        currentNode = self.tail

        while currentNode != self.head:
            print(currentNode.data, end = " <--> ")
            currentNode = currentNode.prev

        print(currentNode.data, end = " <-->")

        print(None)

print("CLL: ")
L3 = CLL()

L3.prepend(4)
L3.prepend(3)
L3.prepend(2)
L3.prepend(1)
L3.prepend(0)
L3.append(5)
L3.append(6)
L3.append(7)
L3.append(8)
L3.printList()              # 0 <--> 1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6 <--> 7 <--> 8 <-->None
L3.print_reverse_List()     # 8 <--> 7 <--> 6 <--> 5 <--> 4 <--> 3 <--> 2 <--> 1 <--> 0 <-->None

L3.delete_end()
L3.printList()              # 0 <--> 1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6 <--> 7 <-->None

L3.delete_start()
L3.printList()              # 1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6 <--> 7 <-->None