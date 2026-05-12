# swap two variables
# using third variable

a = 5
b = 6
temp = a
a = b
b = temp

print(f"The values are a:{a},b:{b}")

# not using third variable
a = 10
b = 12

a,b = b,a
print(f"a:{a},b:{b}")
