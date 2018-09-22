# myList = list(range(101))
# print(myList)
#
# for i in range(0,101):
#     print(i)
#
# even = list(range(0,100,2))
# odd = list(range(1,100,2))
#
# print(even, odd)
#
# myString = "abcdefghijklmnopqrstuvwxyz"
# print(myString.index('e'))
# print(myString[4])

smallDecimals = range(0, 10)
print(smallDecimals)

print(smallDecimals.index(3))

odd2 = range(1, 10000, 2)
print(odd2)

print(odd2[985])

# sevens = range(7, 1000000, 7)
# x = int(input("Input a positive number less than 1.000.000"))
# if x in sevens:
#     print("{} is divisible by 7".format(x))

myRange = smallDecimals[::2]
print(myRange)
print(myRange.index(4))

decimals = range(0, 100)
print(decimals)

myRange = decimals[3:40:3]
print(myRange)

for i in myRange:
    print(i)

print('=' * 40)
for i in range(3, 40, 3):
    print (i)

    print(myRange == range(3, 40, 3))
    