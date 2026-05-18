lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

for i in range(lower,upper+1):
    print(f"2 raised to power {i} is {2**i}")