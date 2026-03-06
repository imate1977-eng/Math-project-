import math

print("MATH TOOLKIT PROJECT")

print("1. HCF and LCM")
print("2. Prime Number Check")
print("3. Quadratic Equation Solver")

choice = int(input("Choose option (1-3): "))

# HCF and LCM
if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    hcf = math.gcd(a,b)
    lcm = (a*b)//hcf
    
    print("HCF =", hcf)
    print("LCM =", lcm)

# Prime number check
elif choice == 2:
    n = int(input("Enter a number: "))
    
    if n < 2:
        print("Not Prime")
    else:
        prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                prime = False
                break
        
        if prime:
            print("Prime Number")
        else:
            print("Not Prime")

# Quadratic equation solver
elif choice == 3:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    
    d = b*b - 4*a*c
    
    if d >= 0:
        root1 = (-b + math.sqrt(d))/(2*a)
        root2 = (-b - math.sqrt(d))/(2*a)
        print("Roots are:", root1, "and", root2)
    else:
        print("No real roots")

else:
    print("Invalid choice")
