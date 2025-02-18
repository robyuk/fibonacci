#! /bin/python3

def fibonacci(n):
    """ This function returns the Nth value in the Fibonacci series, using the iterative method.
     Where F(0)=0,F(1)=1, and F(n)=F(n−1)+F(n−2) for n≥2"""
    if n < 0:
        raise ValueError("Input must be zero or a positive integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# Example usage:
if __name__ == '__main__':
    print(fibonacci(10))  # Output: 55

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
