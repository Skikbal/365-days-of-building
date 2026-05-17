# PROGRAM TO FIND HCF OR GCD
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# def calcHCF(num1,num2):
#     smaller=0
#     hcf = 0
#     if num1 > num2:
#         smaller = num2
#     else:
#         smaller = num1
        
#     for i in range(1,smaller+1):
#         if ((num1%i == 0) and (num2%i == 0)):
#             hcf = i
#     return hcf
# result = calcHCF(num1,num2)
# print("The hcf is ", result)


def calc_hcf(num1,num2):
    smaller = min(num1,num2)
    
    for i in range(smaller,0,-1):
        if num1 % i == 0 and num2 % i == 0:
            return i

result = calc_hcf(num1,num2)

print(result)