import math

# 4
# amount of rice grains on the board:
print(math.pow(1 + 1, 64))

# The globe
radius_earth = 6371
pi = 3.141592653589793
surface_earth = 4*pi*radius_earth**2
rice_grain = 0.000000065

print("Earth's surface: " + str(int(surface_earth)) + "km2")
print(rice_grain * surface_earth)




# 6
items = ['\t', ' ', "a", 'A', 'abc', 'Abc', 'Abcd', '%', 'abcd', '_']

print(items.sort())

# 7
loan = 250000
rentP = loan // 100 * 3
months = 12 * 30
percentage = 1.03 ** (1 / 12)
print("The rent for just one calculation is: " + str(float(rentP)))

print("The amount of months for 30 years is: " + str(months))

print(float(loan) * percentage ** float(months) * (percentage - 1) / (percentage ** months - 1))
