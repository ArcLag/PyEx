name = input("Please enter your name: ")
name2 = input("Please enter your last name:")
age = int(input("How old are you, {0}? ".format(name)))

print(age)

if age >= 18:
    print("You're old enough to vote {0} {1}".format(name, name2))

else:
    print("You're too young to vote, you may participate over {0} years".format(18 - age))
