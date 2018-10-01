import itertools
myList = ["this ", " is ", " a ", " list ", " with ", " the ", " number ", 1]
myTuple = "Halp", "this is a tuple with the number: ", 1
mySet = {1,2,3}, {'a', 'b', 'c'}
print(myList)
print(myTuple)
print(mySet)

differentList = []
differentTuple = " "
differentSet = {4, 5, 6}, {'d', 'e', 'f'}

#color for tuples
# red = 255,0,0
# green = 0,255,0
# blue = 0,0,255

a = {1, 2, 3}
b = {'a', 'b', 'c',2}
print("\n" + "\n" + "\n")
# print(a&b)
# print(a|b)
# print(len(a))
# print(4 in a)
# print(2 in b)
# print(len(a|b))
# print(max(a))
print("\n")


# for i in itertools.product(a,b):
#     print(i)

for i in (a+b):
    print(i)