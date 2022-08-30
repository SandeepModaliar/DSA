
def factorial_non_recursion(n):
    assert n >= 0 and int(n) == n, "Only Positive Integers are allowed"
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

def factorial_recursion(n):
    if n == 1:
        return 1
    else:
        return factorial_recursion(n-1) * n

def factorial_tail_recursion(n, res):
    if n == 1:
        return res
    else:
        return factorial_tail_recursion(n-1, res * n)

print("Factorial using Recursion ")
print(factorial_recursion(10))

print("Factorial with out using Recursion ")
print(factorial_non_recursion(10.5))

print("Factorial using Tail Recursion ")
print(factorial_tail_recursion(10, 1))


