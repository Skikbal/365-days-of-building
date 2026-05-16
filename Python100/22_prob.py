# print all the number divisible by 13
for i in range(1,100):
    if i % 13 == 0:
        print(i)
        continue  
     
     
     
numbers = [13,26,56,72,22,1,11,23,35]

result = list(filter(lambda x:x%13==0,numbers))

print(result)