# Function Scoping Example
x = 10  # Global variable

def scope_example():
    x = 5  # Local variable
    print("Inside function, x =", x)

scope_example()
print("Outside function, x =", x)

# Recursion Example (Factorial)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 is", factorial(5))

# List Mutability Example
def modify_list(lst):
    lst.append(4)

numbers = [1, 2, 3]
modify_list(numbers)
print("Modified list:", numbers)
