shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shoppingList:
    if item == 'spam':
        # print("I am ingoring " + item)
        continue

    print("Buy " + item)

shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shoppingList:
    if item == 'spam':
        # print("I am ingoring and stopping the loop when " + item + " is encountered!")
        break

    print("Buy " + item)

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for x in range(20):
    if x % 3 == 0 or x % 5 == 0:
       continue
    print(x)