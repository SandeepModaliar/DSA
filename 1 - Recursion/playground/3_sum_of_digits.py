def sum_of_digits_recursion(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_recursion(n//10)

def sum_of_digits_tail_recursion(n, sum):
    if n == 0:
        return sum
    else:
        return sum_of_digits_tail_recursion(n//10, sum + n%10)

print("Sum of Digits using Recursion")
print(sum_of_digits_recursion(123456))


print("Sum of Digits using Tail Recursion")
print(sum_of_digits_tail_recursion(123456, 0))