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

# L1 = LL()

# L1.prepend("hi")
# L1.prepend(-10)
# L1.prepend(-30)

# L1.append(0)
# L1.append("bye")
# L1.append(10)
# L1.append(30)
# L1.printList()

# L1.delete_end()
# L1.printList()
# L1.delete_start()
# L1.printList()

# L1.delete_bet(0)
# L1.printList()

# Doubly LL ------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self,data):
        newNode = Node(data)

        if self.head is not None:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode


    def delete_end(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None

        self.tail = self.tail.prev
        self.tail.next = None
    
    # def delete_bet(self, data):
    #     if self.head.data == data:
    #         self.delete_start()

    #     currentNode = self.head

    #     while currentNode.next != None and currentNode.next.data != data:
    #         currentNode = currentNode.next

    #     if currentNode.next is not None:
    #         currentNode.next = currentNode.next.next

    def delete_start(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def printList(self):
        currentNode = self.head

        while currentNode != None:
            print(currentNode.data, end = " <--> ")
            currentNode = currentNode.next

        print(None)

    def print_reverse_List(self):
        currentNode = self.tail

        while currentNode != None:
            print(currentNode.data, end = " <--> ")
            currentNode = currentNode.prev

        print(None)

L2 = DLL()

L2.prepend("hi")
L2.prepend(-10)
L2.prepend(-30)

L2.append(0)
L2.append("bye")
L2.append(10)
L2.append(30)
L2.printList()              # -30 <--> -10 <--> hi <--> 0 <--> bye <--> 10 <--> 30 <--> None
L2.print_reverse_List()     # 30 <--> 10 <--> bye <--> 0 <--> hi <--> -10 <--> -30 <--> None

L2.delete_end()
L2.printList()              # -30 <--> -10 <--> hi <--> 0 <--> bye <--> 10 <--> None

L2.delete_start()
L2.printList()              # -10 <--> hi <--> 0 <--> bye <--> 10 <--> None

# L1.delete_bet(0)
# L1.printList()
