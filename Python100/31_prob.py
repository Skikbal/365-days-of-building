# program to check amstrong number

num = int(input("Enter the number: "))
lenNum = len(str(abs(num)))

sum = 0;

temp = num

while temp > 0:
    digit =temp % 10
    sum += digit ** lenNum
    temp //= 10

if sum == num:
    print("its an amstrong number")
else:
    print("its not an amstrong number")