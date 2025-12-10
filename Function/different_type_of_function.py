# Function With Parameters
def add(a, b):
    print("Sum = "+a + b)

add(5, 6)

# Function With Return Value
def multiply(a, b):
    return a * b

result = multiply(4, 6)
print("Result = ", result)

# Function With Default Parameter
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Sushil")

# Function Returning Multiple Values
def calculate(a, b):
    sum_val = a + b
    diff = a - b
    return sum_val, diff

s, d = calculate(10, 3)
print("Sum =", s)
print("Difference =", d)

# Function With List Processing
def square_list(numbers):
    squares = []
    for n in numbers:
        squares.append(n*n)
    return squares

print(square_list([1, 2, 3, 4]))

# Function Using args (variable number of arguments)
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))
print(total(10, 20))

# Function Using kwargs (variable keyword arguments)
def show_details(**info):
    for key, value in info.items():
        print(key, ":", value)

show_details(name="Sushil", age=21, country="Nepal")

# Lambda Function (Short Inline Function)
square = lambda x: x * x
print(square(5))

# ecursive Function (Function calling itself)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Function Inside Another Function
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()

# Function as an Argument
def shout(text):
    return text.upper()

def process(func):
    print(func("hello world"))

process(shout)





