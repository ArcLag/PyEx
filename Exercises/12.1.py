decimals = range(0, 100)
myRange = decimals[3:40:3]
print(myRange == range(3, 40, 3))
print(range(0, 5, 2) == range(0, 6, 2))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i)

print('=' * 50)
for i in range(99, 0):
    print(i)

print('=' * 50)
print(range(0, 100)[::-2] == range(99, 0, -2))

revString = "egaugnal lufrewop yrev a si nohtyP"
print(revString[::-1])

r = range(0, 10)
for i in r[::-1]:
    print(i)

experiment1 = range(0, -121, -60)
for i in experiment1:
    print(i)

print(experiment1 == range(0, 240, 120))















