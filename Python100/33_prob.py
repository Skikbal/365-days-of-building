n = int(input("Enter the number: "))
sum = 0
# for i in range (1,n+1):
#     sum += i
    
    
# print(sum)

if n < 0:
    print("Enter positive number only")
else:
    while n > 0:
        sum += n
        n -= 1

print(sum)