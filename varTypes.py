# # a = 3
# # b = "123"
# # print(f"{a * b}")


# '''
# so if we have 2 arrays that each one of them 
# has some element that are not repeated and we want to 
# combine these 2 together and also the 2 lits have some common element 
# to get rid of the repeated ones 
# '''
# # list_1 = [1, 2, 3, 6]
# # list_2 = [1, 4, 5, 6]
# # list_1.extend(list_2)
# # combined = list(set(list_1))
# # print(combined)


# # class Parent():
# #     def fun(self):
# #         print("hi")

# # class Child(Parent):
# #     Parent.fun = lambda self: print("Bye")


# # p = Parent()
# # print(p.fun())
# # c = Child()
# # print(c.fun())


# # insertion Sort recursive

# # def insertionSortrecursive(arr, n):
# #     if n == 0:
# #         return
# #     else:
# #         insertionSortrecursive(arr, n-1)
# #         last = arr[n-1]
# #         j = n-2
# #         while j >= 0 and arr[j] > last:
# #             arr[j + 1] = arr[j]
# #             j = j - 1
# #         arr[j+1] = last

# # print(insertionSortrecursive([4,5,6,1,2] ,5))

# '''
# deletion and insertion is more efficient in the linked list than the arrays
# arrays are good at get item and modify it 
# '''