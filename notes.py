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
