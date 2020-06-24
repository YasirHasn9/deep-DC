class Stack:
    def __init__(self):
        self.items = []

    # push is one the fundamentals function in the Stack
    # adds an item on the top of the stack
    def push(self, item):
        self.items.append(item)

    # pop is one the fundamentals function in the Stack
    # will delete the last item been inserted in the stack
    def pop(self):
        self.items.pop()

    def get_stack(self):
        # will return the whole list items
        return self.items

    def get_top(self):
        # return the last item in the stack on the top
        return self.items[-1]
    
    def is_empty(self):
        # just to make sure the list is not empty
        return self.items == []


s = Stack()
print("isEmpty", s.is_empty())
s.push("Book1")
s.push("Book2")
s.push("Book3")
s.push("Book4")
print("1", s.get_top())
print(s.get_stack())

s.pop()
print("2", s.get_top())
print(s.get_stack())
print("isEmpty" , s.is_empty())