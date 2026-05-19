# palindrome
str = "ctcc"

def reverseStr(str):
    listStr = list(str)
    reverseListStr = []
    for i in range(1,len(listStr)+1):
        reverseListStr.append(listStr[-i])
    
    result = "".join(reverseListStr)
    return result
        

result = reverseStr(str)

if result == str:
    print("its palindrome")
else:
    print("its not  valid palindrome")
    
