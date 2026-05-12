# quadratic equation solve a**2 + bx+c = 0

# a,b,c are real number 
# a != 0

# roots = (-b +-sqrt(d)) / (2*a)
# d= (b**2) - (4*a*c)
import cmath

a = int(input("Enter a number (a != 0): "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

# formula for discriminant

d = (b**2) - (4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("The roots are : ",root1,root2)