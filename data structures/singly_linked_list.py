# Estrutura do nó
class Node:
    """
    Each node stores a reference 
    to an object that is an element of the sequence
    """

    def __init__(self, data):    
        self.data = data 
        self.next = None



def add_first(head:Node, data) -> Node:
    """Insert a new node at the beginning of the linked list"""
    new_node = Node(data)
    new_node.next = head
    return new_node


def show_linked_list(head:Node) -> None:
    """Traverse the linked list and print its elements"""
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")



node = Node(5)
node = add_first(node, 4)
node = add_first(node, 3)
node = add_first(node, 2)
node = add_first(node, 1)
show_linked_list(node)


