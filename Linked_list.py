''' Linked list is a list of nodes
             and each node contains data and next
             data = holds the value of the node
             next = points to the next node in the list
    

    there is 2 main pointers in the linked list which one of them 
    points to first item in the list called HEAD and other points to the 
    last node in the list called TAIL
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            # here each time we loop we are moving our current(head) to
            # next node until we reached the (head).next where it points to None
            current_node = current_node.next

    def append(self, data):  # add to the end of the list
        # make a new node to add to the end
        new_node = Node(data)  # now this node the Node.data is whatever we are
        # gonna put in

        # first we need to make sure that the list has some items
        if self.head is None:
            self.head = new_node
            return

        # now we are trying to get the last node in the list
        # of there is more than one node
        last_node = self.head
        # we keep looping over every node in the list since the next
        # of it is not node
        while last_node.next:
            # keep moving the last_node(the head) once we reached
            # the next is pointing to none then stop the loop
            # and make the last_node(the head).next points to none
            last_node = last_node.next

        # since the last_node.next == None , then we have the green light
        # to add the new node to the list
        last_node.next = new_node


    def prepend(self,data):
        # making a new node
        new_node = Node(data)
        
        # making sure that we have an item in the list
        if self.head:
            # make make the next of the new node points to the 
            # self.head
            new_node.next = self.head
            
            # and make the self.head == the new_node
            self.head = new_node


l = LinkedList()
l.append("A")
# print(l.head.data)
l.append("B")
l.append("C")
l.append("D")
l.print_list()
print("one")
l.prepaned("E")
l.print_list()
