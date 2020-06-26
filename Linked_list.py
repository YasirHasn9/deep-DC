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

    def prepend(self, data):
        # making a new node
        new_node = Node(data)

        # making sure that we have an item in the list
        if self.head:
            # make make the next of the new node points to the
            # self.head
            new_node.next = self.head

            # and make the self.head == the new_node
            self.head = new_node

    def insert_after_node(self, prev_node, data):
        # making sure that the prev_node is exited and 
        # next of it point to something
        if not prev_node:
            print("There no pervious node in the list")
            return

# make new node
        new_node = Node(data)
        # make the next of the new node points to the node 
        # that the previous node.next is poiniting to 
        new_node.next = prev_node.next

        # now the new node is pointing to the same node that the pervious node 
        # is pointing 
        # to change that we need to tell the pervious node to point to 
        # the new node 
        prev_node.next = new_node


l = LinkedList()
l.append("A")
# print(l.head.data)
# l.append("B")
l.append("C")
l.append("D")
l.append("E")
l.insert_after_node(l.head.next, "B")
l.print_list()
