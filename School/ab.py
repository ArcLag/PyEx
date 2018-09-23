a = 2
b = -3
c = a+b
d = a//b
print(c)  # -1
print(d)  # -1


# '/' generates floating point numbers/outcomes
# whilst '//' generates integers. % stands for modulo, the remainder of an outcome
s = 0
for i in range(0, 100):
    s += 1
    print(s)

# 6
items = ['\t', ' ', "a", 'A', 'abc', 'Abc', 'Abcd', '%', 'abcd', '_']

print(items.sort())
