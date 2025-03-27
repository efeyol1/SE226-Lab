import math

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


term = lambda n, x: ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

def sine_X(x, n):
    x = math.radians(x)  # Convert degrees to radians
    result = sum(term(i, x) for i in range(n))
    return result

def harmonic_recursive(n, total=0.0):
  
    if n == 0:
        print(f"Harmonic series result: {total}")
        return
    harmonic_recursive(n - 1, total + 1 / n)


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("sin(30) approximation with 5 terms:", sine_X(30, 5))
    print("Harmonic series H5:")
    harmonic_recursive(5)
