# python program display power of 2 using anynomous function

nterms = int(input("Enter number of terms: "))

result = list(map(lambda x: 2**x, range(nterms+1)))
print(result)