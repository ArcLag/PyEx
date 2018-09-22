list1 = []
list2 = list()

print("List 1: {}".format(list1))
print("List 2: {}".format(list2))

if list1 == list2:
    print("The lists are the same")

    even = [2, 4, 6, 8]

another_even = even

print(another_even is even)

another_even.sort(reverse=True)
print(even)

odd = [1, 3, 5, 9]

oddAndEven = [even, odd]

for oddAndEven_set in oddAndEven:
    print(oddAndEven_set)

    for value in oddAndEven_set:
        print(value)
