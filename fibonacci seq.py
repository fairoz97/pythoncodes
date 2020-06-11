import math
def fib(n):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

def fib1(n):
    phi = (math.sqrt(5) + 1 )/2
    return int(((phi**n) - (-phi**(-n)))/(math.sqrt(5)))

n = int(input("Enter number of terms: "))
print("Fib seq:  ")
for i in range(n):
    print(fib1(i))
