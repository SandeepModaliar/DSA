
# 0 1 1 2 3 5 8 13 21 34
def fibonacci_recusion(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci_recusion(n - 1) + fibonacci_recusion(n - 2)


def fibonacci_non_recursion(n):
    f1 = -1
    f2 = 1
    f3 = f1 + f2
    while True:
        f1 = f2
        f2 = f3
        if n == 0:
            break
        f3 = f1 + f2
        n = n - 1
    return f3

def fibonacci_tail_recursion(n, f1, f2):
    if n in [0, 1]:
        return f2
    else:
        return fibonacci_tail_recursion(n - 1, f2, f1 + f2)

print("Fibonacci using Recursion")
print(fibonacci_recusion(7))


print("Fibonacci with out using Recursion")
print(fibonacci_non_recursion(7))


print("Fibonacci with Tail Recursion")
print(fibonacci_tail_recursion(9, -1, 1))
