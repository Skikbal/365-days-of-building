# print the sum of the natural number
# natural number s are the all the posetive integer

num = int(input("Enter the number: "))
if num < 0 :
    print("Enter posetive integer only")
else:   
    sum = 0
    for i in range (1,num+1):
        sum+=i
    print(sum)