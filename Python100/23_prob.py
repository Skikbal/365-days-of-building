# program to convert decimal to binary,octal and hexadecimal

decimal = int(input("Enter the number: "))

binary = bin(decimal)
octal = oct(decimal)
hexad = hex(decimal)

print(f"The conversion of decimal are as follows: binary: {binary}, octal: {octal}, hexadecimal: {hexad}")

