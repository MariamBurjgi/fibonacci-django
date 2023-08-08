# fibonacci_app/fibonacci_generator.py

def generate_fibonacci_iterative(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def generate_fibonacci_recursive(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_sequence = generate_fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
