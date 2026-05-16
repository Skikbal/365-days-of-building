# amstrong program
# it says if we sum the cube of individual digit it is equal to the same number

num = int(input("Enter the number: "))
lenNum = len(str(abs(num)))

temp = num
digit=0
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** lenNum
    temp //= 10

if sum == num:
    print("its an amstrong number")
else:
    print("its not an amstrong number")