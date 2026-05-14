# finding all the prime number in the range

startRange = int(input("Enter the starting range "))
endRange = int(input("Enter the ending range "))
arr = []
for num in range(startRange,endRange+1):
    if num <= 1:
        continue
    for i in range (2,int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        arr.append(num)
    
    
print(arr)