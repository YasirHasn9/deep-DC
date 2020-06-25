'''
The whole idea behind the data structure is to  organize and manage the data 
so we can get an efficient access and modification to it

so there is some ways to deal with ds?
yes for instance 
we can use an array method to get access because it works very well with it
but it bad for insertion or deletion so we are gonna 
use the liked list to insert or delete 
and also both of them are not efficient when it comes to to search in item in list
so we are gonna use the search binary to find an item
'''

# The type of data structure
'''
There 2 types of it 
   A- Primitive Data Structure      B- Non-Primitive Data Structure

                  A- Primitive Data Structure 

    1. Characters    2.Float     3.Integer   4. Pointer   
-----------------------------------------------------------------------


                       B-Non-Primitive Data Structure
        1.Liner data structure                        2. Non_liner data structure
--------------------------------------------------------------------------

    
           1.Liner data structure 
           a.Arrays     b.Liked list    c.Stack     d.Queue
           ------------------------------------------------

           2.Non_liner data structure
           a.Graphs   b.Trees
'''

# Performance
'''
When we start to solve our technical problems, there is some stuff we need be concerned of 
which they are  
                 A.Time                                 B.Space
---------------------------------------------------------------------

Nowdays , the focus is on the Time more that Space because our machines are different from user 
to another 


Example:
Lets say we  have a list of numbers

list = [10,5,15,2,25,55] 

and we want to search for a certain number in the list, if we are lucky we find a the number 
    in the first position list[0] and this is call the best case but in 
    programming there is no such things as luck so we always assume that we are gonna get the worst case
    which is the list[len(list) -1]

or the number could be in the middle of the list and this case called an average case 
----------------------------------------------------------------------------------------

so now we have 3 cases for the time
1.Best Case  Omega              2.Average Case  Theta         3. Worst Case(most important)  Big O Notaion(Order)
'''

# Complexcity
'''
Our mission as programmers is to make the worst case be best case or at least make an average 
but to make this mission easier we need to know the Complexcity of the operation 
------------------------------------------------------------------------------------
for instance if we want to loop over a numbers to get the sum of them
'''
sum = 0
for i in range(0, 6):
    sum += i
# print(sum)

'''
so now we have to get every number between the 0 and 6 to add them up to the sum
for i in range(0,6): --------> this line is O(n)
    sum += i ----------> is O(1) Constant Time which is gonna happend just once

now for-loop(iterations) is a big O(n)
because of this iterations we refere to this operation as O(n)


Time Complexity == O(n) + O(1) =====> O(n)
-----------------------------
'''

'''
lets say you have 
for i in something:
    # this is the outer loop
    // do something
    for j in in somethinElse:
        # this is the inner loop
        // do something else

in this case it is O(n^2)
'''


# Another one
'''
i,n
for(i ; i < n ; i = i*2){
    do something 
}
This is a log(n)
since the operation inside the loop is * or /
'''

# # fibonacci
# def fab(n):
#     print(n)
#     # base case is where the program stops its work
#     if n < 1:
#         return n
#     else:
#         return fab(n / 2)

# print(fab(100))

# def rec(n):
#     if n <= 0 :
#         return 1
#     else:
#         return 1 + rec(n-1)

# print(rec(8))

# Stack
'''

you can think of stack as array, the first item you put in the array 
would the last one who is gonna go out




[
    |c|
    |B|
    |A|
]

since the A is the first one that been inserted inside the stack 
then it would the last one that gonna get out(called)
FILO
or 
LIFO
'''

# Array based implementation
'''
The stack has 4 main functions 
1.push() 
is to add value to the stack

2.pop()
is to delete the last one in the stack(top)

3.getTop()
is to get the last value been insterted in the stack(top)

4.isEmpty()
is to check if the stack is empty
'''
# Stack.py

# Liked List
'''
The best thing about array is that they do have fixed access time O(1)
features of arrays
1.fixed access time
2.sequential
3.bad removal 
4.bad insertion
5.space westage

Now lets talk about the liked list
1.dynamic size
2.no space westage 
3.good removal
4.good insertion
4. sequential space dose not required
5.random access not allowed

SO , How does it work?
 ---Each element in the linked list is been saved certain place in the memory
    and is not necessary to be sequential

How can i recognize them in the memory ?
--- Each item is made of a value and a pointer , inside in the pointer would the address of the next
item in the linked list. We are gonna call this combination A Node
item + pointer = Node
class Node:
    def __init__(self, value, next)
'''


# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.next = None


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_to_head(self, value):
        newNode = Node(value)
        # if there no node in the list
        if not self.head:
            self.head = newNode
            newNode.next = None
        else:
            # now we are just change the pointer of the nex node to old item
            # or the item before the newNode
            newNode.next = self.head
            # make the head points of the first node in the list
            self.head = newNode

    def add_to_tail(self, value):
        newNode = Node(value)
        # first we check if the if the tail.next == none
        # since it is the last item in the linkedlist
        if self.tail.next is None:
            # now we have to make the tail is the newNode 
            # by pointing the next of the tail to the new one
            self.tail.next = newNode
            # sine the newNode is last one in the list so the next of the newNode 
            # should points to None
            newNode.next = None
            # also we should make sure that the tail points at the 
            # node in the list
            self.tail = newNode


# a = [1,2,3,4]
# b = [1,3,5,6]
# a.extend(b)
# print(list(set(a)))

# def insertSortArr(arr ,  n):
#     if n == 2:
#         return
#     else:
#         insertSortArr(arr,n-1)
#         last = arr[n-1]
#         j = n - 2
#         while(j >= 0 and arr[j] > last):
#             arr[j+1] = arr[j]
#             j= j -1
#         arr[j+1] = last

# print(insertSortArr([2,5,2,6,7,3,4],5))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_first(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            newNode.next = None
        else:
            newNode.next = self.head
            self.head = newNode
