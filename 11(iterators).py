string = "1234567890"

# myIterator = iter(string)
# print(myIterator)

# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
#
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numberListIterator = iter(numberList)

print(len(numberList))
print(numberList)

for i in range(0, len(numberList)):
    nextItem = next(numberListIterator)
    print(nextItem)
# for entries in numberIterator:
#     print
