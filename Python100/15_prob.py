number = int(input("Enter the input "))

if number == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range (1,number+1):
        factorial*=i
    
    print(factorial)