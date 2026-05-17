# program to display fibonacci series using recurssion

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

nterms = int(input("Enter the number of terms: "))

for i in range(nterms):
    print(fibonacci(i))