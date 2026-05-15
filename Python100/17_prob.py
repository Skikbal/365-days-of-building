num = int(input("Enter the number: "))

for i in range (1,num+1):
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}")
        

# using while loop find table of a number
i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i+=1