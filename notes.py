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
for i in range(0,6):
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


                                       #Stack
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