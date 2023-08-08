
from django.shortcuts import render
from .fibonacci_generator import generate_fibonacci_iterative, generate_fibonacci_recursive

def fibonacci_view(request):
    n = 10  # Default value
    fib_iterative = generate_fibonacci_iterative(n)
    fib_recursive = generate_fibonacci_recursive(n)

    if request.method == 'POST':
        n = int(request.POST.get('number', 10))
        fib_iterative = generate_fibonacci_iterative(n)
        fib_recursive = generate_fibonacci_recursive(n)

    context = {
        'n': n,
        'fib_iterative': fib_iterative,
        'fib_recursive': fib_recursive,
    }
    return render(request, 'fibonacci_app/fibonacci.html', context)



