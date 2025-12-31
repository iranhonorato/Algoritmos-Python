# Estrutura do nó
class Node:
    """
    each node stores a reference 
    to an object that is an element of the sequence
    """

    def __init__(self, value):    
        self.value = value 
        self.next = None





# Estrutua da singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.size = 0

    def add_first(self, value):
        """
        add_first(10)
        [10] → None

        add_first(5)
        [5] → [10] → None
        """
        node = Node(value)
        node.next = self.head
        self.head = node 
        self.size += 1 
