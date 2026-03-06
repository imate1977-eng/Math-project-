# Simple Math Calculator

import math

print("Math Project Calculator")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("HCF =", math.gcd(a,b))
print("LCM =", (a*b)//math.gcd(a,b))
