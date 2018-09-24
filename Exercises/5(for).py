for i in range(1,20):
    print("it is {}".format(i))

number = "9,223,372,036,854,775,807"
for i in range (0,len(number)):
    print(number[i], end='\t')

number = "9,223,372,036,854,775,807"

cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]
        #print(number[i],end='')

        newNumber = int(cleanedNumber)

print("the number is {}".format(newNumber))