# program to find amstrong number in an interval

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for i in range(num1,num2+1):
    lenNum = len(str(abs(i)))
    temp = i
    sum=0
    while temp > 0:
        digit = temp%10
        sum = digit ** lenNum
        temp //= 10
    if sum == i:
        print(i)
    else:
        continue